def map_workflow(saved_config):
    default_workflow = {
        "workflow_name": "default",
        "workflow": [
            {
                "index": "1",
                "input": [
                    "input_url"
                ],
                "name": "scrape_input_url",
                "type": "scrape",
                "parameters": {
                    "search_engine": "",
                    "search_queries": "",
                    "search_per_quiry": "",
                    "crawler_mode": False,
                    "max_scraped_token": 10000
                },
                "output": "scraped_input_url"
            },
            {
                "index": "2",
                "input": [
                    "input_url",
                    "scraped_input_url"
                ],
                "name": "llm_get_company_name",
                "type": "llm",
                "parameters": {
                    "model_type": "bedrock",
                    "prompt_type": "single-prompt",
                    "inference": {
                        "body": {
                            "prompt": "\n\nHuman: From the following text that has been scraped from webpage {workflow_inputs['input_url']}. What is the name of the company.\nReturn only the company name and nothing else.\n\n<web_data>{workflow_inputs['scraped_input_url']}</web_data>\n\nAssistant: The company name is\n\n",
                            "max_tokens_to_sample": 10
                        },
                        "modelId": "anthropic.claude-instant-v1",
                        "accept": "application/json",
                        "contentType": "application/json"
                    },
                    "format": "string"
                },
                "output": "company_name"
            },
            {
                "index": "3",
                "input": [
                    "input_url",
                    "company_name"
                ],
                "name": "search_company_info",
                "type": "scrape",
                "parameters": {
                    "search_engine": "bing",
                    "search_queries": [
                        "{workflow_inputs['company_name']} About",
                        "{workflow_inputs['company_name']} Financial",
                        "{workflow_inputs['company_name']} Service"
                    ],
                    "search_per_quiry": "3",
                    "crawler_mode": False,
                    "max_scraped_token": 10000
                },
                "output": "company_info"
            },
            {
                "index": "4",
                "type": "parallel",
                "branches": [
                    {
                        "branch_name": "introduction",
                        "branch_workflow": [
                            {
                                "index": "4.1.1",
                                "input": [
                                    "company_name",
                                    "company_info"
                                ],
                                "name": "llm_generate_introduction",
                                "type": "llm",
                                "parameters": {
                                    "model_type": "bedrock",
                                    "prompt_type": "claude multi-prompt",
                                    "inference": {
                                        "body": {
                                            "prompt": {
                                                "p_human": "\n\nHuman: ",
                                                "p_task_context": "\n\nYou are the helpful and expert researcher for the board of directors. You are judged on the accuracy of your work and the insighful analysis behind it. Your goal is to analyse the given documents and write the introduction section of the report",
                                                "p_tone_context": "\n\nBe exhaustive and use thesis-antithesis-synthesis to formulate the response. Be very critical, concise, constructive and avoid Repetition.",
                                                "p_data": "\n\nI'm going to give you some documents of web scraping data for a company called {workflow_inputs['company_name']}. Read the documents carefully, because I'm going to ask you a question about it. Here are the documents: <document>{workflow_inputs['company_info']}</document>",
                                                "p_task_description": "\n\nWrite an introduction section of {workflow_inputs['company_name']} company report. The introduction section will contain only these five fields. <Name>, <Type>, <Sector>, <Business Overview> <Proposition>.",
                                                "p_example": "",
                                                "p_conversation_history": "",
                                                "p_thought_process": "\n\nThink about your answer first before you respond. Take a deep breath. Silently go through each task step by step",
                                                "p_formatting": "\n\nReturn data in the following json format\n\"introduction\":{\n\"name\":\"\",\n\"type\":\"\",\n\"sector\":\"\",\n\"business_overview\":\"\",\n\"proposition\":\"\"\n}",
                                                "p_assistant": "\n\nAssistant:{"
                                            },
                                            "max_tokens_to_sample": 20000
                                        },
                                        "modelId": "anthropic.claude-instant-v1",
                                        "accept": "application/json",
                                        "contentType": "application/json"
                                    },
                                    "format": "json"
                                },
                                "output": "introduction_report"
                            }
                        ]
                    },
                    {
                        "branch_name": "financial",
                        "branch_workflow": [
                            {
                                "index": "4.2.1",
                                "input": [
                                    "input_url",
                                    "company_name"
                                ],
                                "name": "search_financial",
                                "type": "scrape",
                                "parameters": {
                                    "search_engine": "bing",
                                    "search_queries": [
                                        "{workflow_inputs['company_name']} Highlight Financial Overtime",
                                        "{workflow_inputs['company_name']} New Product/Services Roadmaps",
                                        "{workflow_inputs['company_name']} Annual Report",
                                        "{workflow_inputs['company_name']} Company Structure"
                                    ],
                                    "search_per_quiry": "3",
                                    "crawler_mode": False,
                                    "max_scraped_token": 10000
                                },
                                "output": "financial_info"
                            },
                            {
                                "index": "4.2.2",
                                "input": [
                                    "company_name",
                                    "financial_info"
                                ],
                                "name": "llm_generate_financial",
                                "type": "llm",
                                "parameters": {
                                    "model_type": "bedrock",
                                    "prompt_type": "claude multi-prompt",
                                    "inference": {
                                        "body": {
                                            "prompt": {
                                                "p_human": "\n\nHuman: ",
                                                "p_task_context": "\n\nYou are the helpful and expert researcher for the board of directors. You are judged on the accuracy of your work and the insighful analysis behind it. Your goal is to analyse the given documents and write the business health section of the report",
                                                "p_tone_context": "\n\nBe exhaustive and use thesis-antithesis-synthesis to formulate the response. Be very critical, concise, constructive and avoid Repetition.",
                                                "p_data": "\n\nI'm going to give you some documents of web scraping data for a company called {workflow_inputs['company_name']}. Read the documents carefully, because I'm going to ask you a question about it. Here are the documents: <document>{workflow_inputs['financial_info']}</document>",
                                                "p_task_description": "\n\nWrite a business health section of {workflow_inputs['company_name']} company report. The business health section section will contain only these four fields. <Headline financial overtime>, <Company Structure>, <Highlight from last annual report>, <Service and roadmaps>.\nBe descriptive",
                                                "p_example": "",
                                                "p_conversation_history": "",
                                                "p_thought_process": "\n\nThink about your answer first before you respond. Take a deep breath. Silently go through each task step by step",
                                                "p_formatting": "\n\nReturn data in the following json format\n\"business_health\":{\n\"headline_financial_overtime\":\"\",\n\"company_structure\":\"\",\n\"last_annual_report\":\"\",\n\"service_roadmaps\":\"\"\n}",
                                                "p_assistant": "\n\nAssistant:{"
                                            },
                                            "max_tokens_to_sample": 20000
                                        },
                                        "modelId": "anthropic.claude-instant-v1",
                                        "accept": "application/json",
                                        "contentType": "application/json"
                                    },
                                    "format": "json"
                                },
                                "output": "financial_report"
                            }
                        ]
                    },
                    {
                        "branch_name": "audience",
                        "branch_workflow": [
                            {
                                "index": "4.3.1",
                                "input": [
                                    "input_url",
                                    "company_name"
                                ],
                                "name": "search_audience",
                                "type": "scrape",
                                "parameters": {
                                    "search_engine": "bing",
                                    "search_queries": [
                                        "{workflow_inputs['company_name']} target demographic audience",
                                        "{workflow_inputs['company_name']} target geographic audience",
                                        "{workflow_inputs['company_name']} target sector audience"
                                    ],
                                    "search_per_quiry": "3",
                                    "crawler_mode": False,
                                    "max_scraped_token": 10000
                                },
                                "output": "audience_info"
                            },
                            {
                                "index": "4.3.2",
                                "input": [
                                    "company_name",
                                    "audience_info"
                                ],
                                "name": "llm_generate_audience",
                                "type": "llm",
                                "parameters": {
                                    "model_type": "bedrock",
                                    "prompt_type": "claude multi-prompt",
                                    "inference": {
                                        "body": {
                                            "prompt": {
                                                "p_human": "\n\nHuman: ",
                                                "p_task_context": "\n\nYou are the helpful and expert researcher for the board of directors. You are judged on the accuracy of your work and the insighful analysis behind it. Your goal is to analyse the given documents and write the target audience section of the report",
                                                "p_tone_context": "\n\nBe exhaustive and use thesis-antithesis-synthesis to formulate the response. Be very critical, concise, constructive and avoid Repetition.",
                                                "p_data": "\n\nI'm going to give you some documents of web scraping data for a company called {workflow_inputs['company_name']}. Read the documents carefully, because I'm going to ask you a question about it. Here are the documents: <document>{workflow_inputs['audience_info']}</document>",
                                                "p_task_description": "\n\nWrite an target audience section of {workflow_inputs['company_name']} company report. The target audience section section will contain only these three fields. <target demogrophic>, <target geographic>, <target sector>.\nBe descriptive, include reasons why they are target audience. Don't just list them",
                                                "p_example": "",
                                                "p_conversation_history": "",
                                                "p_thought_process": "\n\nThink about your answer first before you respond. Take a deep breath. Silently go through each task step by step",
                                                "p_formatting": "\n\nReturn data in the following json format\n\"audience\":{\n\"demogrophic\":\"\",\n\"geographic\":\"\",\n\"sector\":\"\"\n}",
                                                "p_assistant": "\n\nAssistant:{"
                                            },
                                            "max_tokens_to_sample": 20000
                                        },
                                        "modelId": "anthropic.claude-instant-v1",
                                        "accept": "application/json",
                                        "contentType": "application/json"
                                    },
                                    "format": "json"
                                },
                                "output": "audience_report"
                            }
                        ]
                    },
                    {
                        "branch_name": "competitors",
                        "branch_workflow": [
                            {
                                "index": "4.3.1",
                                "input": [
                                    "company_name",
                                    "company_info"
                                ],
                                "name": "llm_company_summary",
                                "type": "llm",
                                "parameters": {
                                    "model_type": "bedrock",
                                    "prompt_type": "claude multi-prompt",
                                    "inference": {
                                        "body": {
                                            "prompt": {
                                                "p_human": "\n\nHuman: ",
                                                "p_task_context": "\n\nYou are the helpful and expert researcher for the board of directors. You are judged on the accuracy of your work and the insighful analysis behind it. Your goal is to analyse the given documents and write single paragraph that defines their business sufficiently so that I can perform a competitive review.",
                                                "p_tone_context": "",
                                                "p_data": "\n\nI'm going to give you some documents of web scraping data for a company called {workflow_inputs['company_name']}. Read the documents carefully, because I'm going to ask you a question about it. Here are the documents: <document>{workflow_inputs['company_info']}</document>",
                                                "p_task_description": "\n\nWrite a single paragraph that defines {workflow_inputs['company_name']} company business sufficiently so that I can perform a competitive review.\nDo not reference the name of the company directly.\nThe paragraph should include things like provide services or products, sector, target audience, scale of client (S,M,L,XL),  and whatever else is required to be able to compare like with like.\nDo not reference the name of the company directly.\nDo not reference the name of the company directly.",
                                                "p_example": "",
                                                "p_conversation_history": "",
                                                "p_thought_process": "\n\nThink about your answer first before you respond. Take a deep breath. Silently go through each task step by step",
                                                "p_formatting": "",
                                                "p_assistant": "\n\nAssistant:"
                                            },
                                            "max_tokens_to_sample": 20000
                                        },
                                        "modelId": "anthropic.claude-instant-v1",
                                        "accept": "application/json",
                                        "contentType": "application/json"
                                    },
                                    "format": "text"
                                },
                                "output": "company_summary"
                            },
                            {
                                "index": "4.3.2",
                                "input": [
                                    "company_summary",
                                ],
                                "name": "llm_company_client_POV",
                                "type": "llm",
                                "parameters": {
                                    "model_type": "bedrock",
                                    "prompt_type": "claude multi-prompt",
                                    "inference": {
                                        "body": {
                                            "prompt": {
                                                "p_human": "\n\nHuman: ",
                                                "p_task_context": "\n\nYou are the helpful and expert researcher for the board of directors. You are judged on the accuracy of your work and the insighful analysis behind it. Your goal is to analyse the given documents and give insight from the perspective of potential clients",
                                                "p_tone_context": "",
                                                "p_data": "\n\nI'm going to give you some documents of company summary. Read the documents carefully, because I'm going to ask you a question about it. Here are the documents: <document>{workflow_inputs['company_summary']}</document>",
                                                "p_task_description": "\n\nFrom a POV of potential clients of the above company, write a brief that would lead you to them, what kind of products or services you were looking for, what challenge were you facing that leads you to approach the company.\nLimit the brief to key bullet points.\nDo not reference the name of the company directly.",
                                                "p_example": "\n\nHere is an example of how to write the brief:\n<example>Q: User given some documents about draft beer company.\nA:\n- Looking for an established brewery with a strong background in craft beer and a reputation for quality IPAs and seasonal offerings.\n- Desire a supplier that can handle large-scale orders while still offering a variety of unique and distinctive beer flavors.\n- Interested in a brewery that retains a creative and artisanal approach to beer-making despite significant operational growth.\n- Require a partner with a potentially expanded beverage portfolio for diverse market needs, thanks to recent ownership changes.\n- Value a brewer that can provide a craft brew experience that appeals to a discerning beer enthusiast customer base.\n- Seek a dependable and scalable beer supply source with an artistic heritage and recognition in the market.\n- Prefer working with a brewery that has benefitted from investment in facilities to accommodate increased production demands.\n- As a potential client, anticipate a balance of tradition and innovation in brewing techniques and flavor profiles.\n- Looking to develop a relationship with a brewery that has transitioned smoothly from local to major player in the industry and is backed by a strong multinational corporation.</example>",
                                                "p_conversation_history": "",
                                                "p_thought_process": "\n\nThink about your answer first before you respond. Take a deep breath. Silently go through each task step by step",
                                                "p_formatting": "",
                                                "p_assistant": "\n\nAssistant:"
                                            },
                                            "max_tokens_to_sample": 20000
                                        },
                                        "modelId": "anthropic.claude-instant-v1",
                                        "accept": "application/json",
                                        "contentType": "application/json"
                                    },
                                    "format": "text"
                                },
                                "output": "company_client_POV"
                            }
                        ]
                    }
                ],
                "output": "llm_report"
            }
        ],
    }

    workflow_name = "_".join([key for key, value in saved_config.items() if value])
    default_workflow["workflow_name"] = workflow_name

    parallel_step = default_workflow["workflow"][3]

    # Check if all workflow options are False, indicating no branch should be included
    if not any(saved_config.values()):
        default_workflow["workflow"] = default_workflow["workflow"][
            :3
        ]  # Remove the parallel step
    else:
        # Remove branches based on user-selected workflow
        if not saved_config["Introduction"]:
            parallel_step["branches"] = [
                branch
                for branch in parallel_step["branches"]
                if branch["branch_name"] != "introduction"
            ]
        if not saved_config["Business Health"]:
            parallel_step["branches"] = [
                branch
                for branch in parallel_step["branches"]
                if branch["branch_name"] != "financial"
            ]
        if not saved_config["Audiences"]:
            parallel_step["branches"] = [
                branch
                for branch in parallel_step["branches"]
                if branch["branch_name"] != "audience"
            ]
        if not saved_config["Competitors"]:
            parallel_step["branches"] = [
                branch
                for branch in parallel_step["branches"]
                if branch["branch_name"] != "competitors"
            ]

    return default_workflow, workflow_name
