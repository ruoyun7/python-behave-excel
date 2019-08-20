Feature: 开票模块
  Scenario Outline: 开票
    Then 拆分成功测试用例 <testId> and <noticeId> and <invoiceType> and <noticeOpenToken> and <count>

  Examples: all request type
  |testId |noticeId         |invoiceType|noticeOpenToken                          |count
  |1001   |340796193636352 |ZZSPTFP     |2354f857-029d-45a6-8189-889b50983df7|  5
  |1002   |340796193636352 |ZZSPTFP     |2354f857-029d-45a6-8189-889b50983df7|  5




