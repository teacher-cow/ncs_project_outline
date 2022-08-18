# text_extract API

## API Documentation

**http://localhost:8000/docs**

## API Specification

**URL: /text_extract**

**Type: POST**

**Description**

do a simple entity extraction on the text body

**Sample URL** 

```
http://{AppUri}/text_extract
```

**Input**
Field   type     Description
------------------------------
|text  | String |  Required  |

**Sample Input** 
{"text":"今天深圳的天气真好呀"}

**Output**
Field   type     Description
------------------------------
|result  | List | List of extract result  |

**Sample Output**

{
  "result": [
    "天气",
    "深圳"
  ]
}

