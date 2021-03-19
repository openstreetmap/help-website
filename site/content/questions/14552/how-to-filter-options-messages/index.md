+++
type = "question"
title = "How to filter OPTIONS messages"
description = '''Hi All, To filter out OPTIONS message in wireshark traces, I could not find a way. Whatever I tried, broke another thing and since there are too many OPTIONS heartbeat message and 200 OK response to these message, I need to filter them out for sure. I tried these 2 things too add in addition to &quot;cam...'''
date = "2012-09-26T13:13:00Z"
lastmod = "2012-09-26T15:48:00Z"
weight = 14552
keywords = [ "filter", "options" ]
aliases = [ "/questions/14552" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter OPTIONS messages](/questions/14552/how-to-filter-options-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14552-score" class="post-score" title="current number of votes">0</div><span id="post-14552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>To filter out OPTIONS message in wireshark traces, I could not find a way. Whatever I tried, broke another thing and since there are too many OPTIONS heartbeat message and 200 OK response to these message, I need to filter them out for sure.</p><p>I tried these 2 things too add in addition to "camel || inap || tcap || sip" filter</p><p>1- When I tried to add below sentence to the filters, it also filters 180 Ringing messages, that I do not know why. sip.Method != "OPTIONS"</p><p>2- When I tried to add below sentence to the filters, it shows all messages except OPTIONS messages including TCP IP, ARP, Heartbeat messages.</p><p>!(sip.Method == "OPTIONS")</p><p>I would appreciate for your assitance, thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '12, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/8a89adee5542993469b705f8b02eb58f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="optionsboy&#39;s gravatar image" /><p><span>optionsboy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="optionsboy has no accepted answers">0%</span></p></div></div><div id="comments-container-14552" class="comments-container"></div><div id="comment-tools-14552" class="comment-tools"></div><div class="clear"></div><div id="comment-14552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14553"></span>

<div id="answer-container-14553" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14553-score" class="post-score" title="current number of votes">2</div><span id="post-14553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="optionsboy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here is what both filters mean:</p><ol><li>sip.Method != "OPTIONS" means "There is at least one sipMethod field that does not have the value 'OPTIONS'"</li><li>!(sip.Method == "OPTIONS") means "There is no sipMethod field that has the value 'OPTIONS'"</li></ol><p>So in 1) there needs to be a sip.Method field to make the filter match, while in 2) there does not need to be a sip.Method field present.</p><p>How about the filter <code>sip.Method &amp;&amp; !(sip.Method == "OPTIONS")</code> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '12, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14553" class="comments-container"><span id="14554"></span><div id="comment-14554" class="comment"><div id="post-14554-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. But I already tried also -&gt; sip.Method &amp;&amp; !(sip.Method == "OPTIONS")</p><p>this is not filtering 200 OK responses to OPTIONS message. This is just filtering OPTIONS messages. As I told there are too many OPTIONS and 200 OK messages as a response to these messages. I need to filter out 2 of them</p><p>I do not want to filter all 200 OK messages, just the ones which are responses to OPTIONS messages</p></div><div id="comment-14554-info" class="comment-info"><span class="comment-age">(26 Sep '12, 14:15)</span> <span class="comment-user userinfo">optionsboy</span></div></div><span id="14555"></span><div id="comment-14555" class="comment"><div id="post-14555-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment, please review the FAQ for details)</p><p>Wireshark filters work on PDUs and a request is one PDU and the response is another. So wireshark can not filter the "200 OK" messages in the way you want by default.</p><p>However, with <a href="http://wiki.wireshark.org/Mate">MATE</a>, you can indeed link requests to responses and create a filter that only deletes the SIP messages of method OPTIONS and the corresponding responses. I do not have a MATE script ready for that though, you will need to cook one yourself based on the (limited) examples provided.</p></div><div id="comment-14555-info" class="comment-info"><span class="comment-age">(26 Sep '12, 14:28)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="14558"></span><div id="comment-14558" class="comment"><div id="post-14558-score" class="comment-score"></div><div class="comment-text"><p>I have no information about MATE script. I could not find enough example for me to create a one.</p><p>So, still I need an answer, if some has already tried this. Because, this should be a popular filtering in all SIP messaging networks.</p><p>so for now sip.Method != "OPTIONS" filter is better for me because it was filtering all OPTIONS and 200 OK response to OPTIONS message, but it is also filtering some extra messages which includes the word "options"...</p></div><div id="comment-14558-info" class="comment-info"><span class="comment-age">(26 Sep '12, 14:46)</span> <span class="comment-user userinfo">optionsboy</span></div></div><span id="14559"></span><div id="comment-14559" class="comment"><div id="post-14559-score" class="comment-score"></div><div class="comment-text"><p>I just downloaded a SIP trace from <a href="http://www.pcapr.net">www.pcapr.net</a>, in this trace both requests and responses have the sip.CSeq.method field. Does your SIP traffic has that field too? If it does, you might be able to achieve your goal with:</p><pre><code>sip &amp;&amp; !(sip.CSeq.method == &quot;OPTIONS&quot;)</code></pre></div><div id="comment-14559-info" class="comment-info"><span class="comment-age">(26 Sep '12, 15:10)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="14563"></span><div id="comment-14563" class="comment"><div id="post-14563-score" class="comment-score"></div><div class="comment-text"><p>Thanks a million</p></div><div id="comment-14563-info" class="comment-info"><span class="comment-age">(26 Sep '12, 15:48)</span> <span class="comment-user userinfo">optionsboy</span></div></div></div><div id="comment-tools-14553" class="comment-tools"></div><div class="clear"></div><div id="comment-14553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

