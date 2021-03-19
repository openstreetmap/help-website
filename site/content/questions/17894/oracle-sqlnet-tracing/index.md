+++
type = "question"
title = "Oracle SQLNET Tracing"
description = '''Hello! This question is about using Wireshark to read the contents of TNS packets. I have no problem tracing an Oracle session, decoding the TNS, and finding the query text (select from some table). What puzzles me is why I see &quot;ORA-01403: no data found&quot; in the response from the database server even...'''
date = "2013-01-23T05:10:00Z"
lastmod = "2013-01-24T16:13:00Z"
weight = 17894
keywords = [ "sqlnet", "tns" ]
aliases = [ "/questions/17894" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Oracle SQLNET Tracing](/questions/17894/oracle-sqlnet-tracing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17894-score" class="post-score" title="current number of votes">0</div><span id="post-17894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>This question is about using Wireshark to read the contents of TNS packets. I have no problem tracing an Oracle session, decoding the TNS, and finding the query text (select from some table). What puzzles me is why I see "ORA-01403: no data found" in the response from the database server even when the query has a result set. Have I missed a set-up step? I am evaluating the use of SQLNET encryption, but first I want to understand the problem.</p><p>Thank you for your help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sqlnet" rel="tag" title="see questions tagged &#39;sqlnet&#39;">sqlnet</span> <span class="post-tag tag-link-tns" rel="tag" title="see questions tagged &#39;tns&#39;">tns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '13, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/b30534debd97f72d5b42b118f256543d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thomaswireshark&#39;s gravatar image" /><p><span>thomaswireshark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thomaswireshark has no accepted answers">0%</span></p></div></div><div id="comments-container-17894" class="comments-container"></div><div id="comment-tools-17894" class="comment-tools"></div><div class="clear"></div><div id="comment-17894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17905"></span>

<div id="answer-container-17905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17905-score" class="post-score" title="current number of votes">0</div><span id="post-17905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have not looked at TNS packets much, but could it be that SQLNET is iterating through the rows of the query result and gives this message after the last row?</p><p>Anyways, this seems a little off topic to me as it is more of a SQLNET question than a Wireshark Question...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '13, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17905" class="comments-container"><span id="17908"></span><div id="comment-17908" class="comment"><div id="post-17908-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your reply and idea, a good one. I can be more specific with my question. Wireshark dissects the column headers (labels, names), but gives "data not found" instead of data. I wonder if the dissector source might have some clues to what Wireshark displays? Perhaps I could also put this post more on topic by rephrasing the question to ask how I can use Wireshark to view full TNS payloads. Here is what I have for the Wireshark TNS dissector code:</p><p><a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-tns.c">http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-tns.c</a></p></div><div id="comment-17908-info" class="comment-info"><span class="comment-age">(23 Jan '13, 13:28)</span> <span class="comment-user userinfo">thomaswireshark</span></div></div><span id="17909"></span><div id="comment-17909" class="comment"><div id="post-17909-score" class="comment-score"></div><div class="comment-text"><p>As the string "Data not found" is not present in the dissector, might it be a literally string in the SQLNET output?</p><p>Are you able to share the tracefile on www.cloudshark.org or does it contain sensitive data?</p></div><div id="comment-17909-info" class="comment-info"><span class="comment-age">(23 Jan '13, 13:38)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="17913"></span><div id="comment-17913" class="comment"><div id="post-17913-score" class="comment-score"></div><div class="comment-text"><p>I have pretty much figured this out. My test was on a single-row table with a single numeric column. It appears that Wireshark balks at numbers in the SQLNET payload. I base this statement on the fact that the number appeared in the packet payload after I converted it to a character in the SQL. In my first test, it only appeared that I was not getting any data; in fact, the "ORA-01403: no data found" only means "end of data" basically - as you astutely suggested. So certainly it is true that without SQLNET encryption all that sensitive Oracle HR data travels in the clear. Thanks for your help!</p></div><div id="comment-17913-info" class="comment-info"><span class="comment-age">(23 Jan '13, 16:42)</span> <span class="comment-user userinfo">thomaswireshark</span></div></div><span id="17916"></span><div id="comment-17916" class="comment"><div id="post-17916-score" class="comment-score"></div><div class="comment-text"><p>Interesting ... It's not Wireshark, or, for that matter, Netmon. Direct SQLNET client tracing in Oracle produces the same results: numbers and dates do not show in the trace results unless you first convert them to character format (TO_CHAR) in the SQL.</p></div><div id="comment-17916-info" class="comment-info"><span class="comment-age">(23 Jan '13, 17:41)</span> <span class="comment-user userinfo">thomaswireshark</span></div></div></div><div id="comment-tools-17905" class="comment-tools"></div><div class="clear"></div><div id="comment-17905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17944"></span>

<div id="answer-container-17944" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17944-score" class="post-score" title="current number of votes">0</div><span id="post-17944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When doing a selece query, ORA no data found message indicate that you're at the end of your query (last row of your query). So it's not an error or anything. Are you troubleshooting an issue or just curious about the no data found message?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '13, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-17944" class="comments-container"></div><div id="comment-tools-17944" class="comment-tools"></div><div class="clear"></div><div id="comment-17944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

