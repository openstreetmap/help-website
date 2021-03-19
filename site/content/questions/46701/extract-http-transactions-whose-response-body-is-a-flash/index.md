+++
type = "question"
title = "extract HTTP transactions whose response body is a flash"
description = '''In a pcap with many HTTP transactions, wonder if there is a way to extract the transactions whose response body starts with 3 characters &quot;CWS&quot; (Adobe flash). It is frequently used to deliver malware.'''
date = "2015-10-19T09:33:00Z"
lastmod = "2015-10-20T07:25:00Z"
weight = 46701
keywords = [ "wireshark" ]
aliases = [ "/questions/46701" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [extract HTTP transactions whose response body is a flash](/questions/46701/extract-http-transactions-whose-response-body-is-a-flash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46701-score" class="post-score" title="current number of votes">0</div><span id="post-46701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a pcap with many HTTP transactions, wonder if there is a way to extract the transactions whose response body starts with 3 characters "CWS" (Adobe flash). It is frequently used to deliver malware.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-46701" class="comments-container"></div><div id="comment-tools-46701" class="comment-tools"></div><div class="clear"></div><div id="comment-46701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="46716"></span>

<div id="answer-container-46716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46716-score" class="post-score" title="current number of votes">0</div><span id="post-46716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe something like this:</p><pre><code>http.content_type == &quot;application/x-shockwave-flash&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46716" class="comments-container"><span id="46733"></span><div id="comment-46733" class="comment"><div id="post-46733-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the idea. It works when server sent that in the HTTP response. But malware servers may not be that honest :-(</p></div><div id="comment-46733-info" class="comment-info"><span class="comment-age">(19 Oct '15, 17:09)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="46746"></span><div id="comment-46746" class="comment"><div id="post-46746-score" class="comment-score"></div><div class="comment-text"><p><span>@pktUser1001</span>: Really ;)</p></div><div id="comment-46746-info" class="comment-info"><span class="comment-age">(19 Oct '15, 23:52)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-46716" class="comment-tools"></div><div class="clear"></div><div id="comment-46716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46720"></span>

<div id="answer-container-46720" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46720-score" class="post-score" title="current number of votes">0</div><span id="post-46720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the folowing display filters finding the streams (maybe if you use tshark)</p><pre><code> media matches &quot;CWS.*&quot;</code></pre><p>or the filter which Jaap has posted.</p><p>Also you can export the flash content with the following dialog: File -&gt; Export objects -&gt; HTTP</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ExportFlash_1NvDRSz.PNG" alt="alt text" /> This dialog shows you all the Obeject inside the HTTP streams and you are able to export(extract) their contents.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '15, 14:20</strong> </span></p></div></div><div id="comments-container-46720" class="comments-container"><span id="46734"></span><div id="comment-46734" class="comment"><div id="post-46734-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@Christian_R</span> for the tips, as mentioned earlier, it may not always have the right content-type in the server response since it's malware traffic.</p></div><div id="comment-46734-info" class="comment-info"><span class="comment-age">(19 Oct '15, 17:11)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="46738"></span><div id="comment-46738" class="comment"><div id="post-46738-score" class="comment-score"></div><div class="comment-text"><p><code>media matches "CWS.*"</code> was able to catch the HTTP response, thanks for that! Wish it could catch the matching HTTP request as well.</p></div><div id="comment-46738-info" class="comment-info"><span class="comment-age">(19 Oct '15, 17:29)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="46743"></span><div id="comment-46743" class="comment"><div id="post-46743-score" class="comment-score"></div><div class="comment-text"><p>It is not so easy with just a blind filter. One way is to filter out the (ip.clientaddr)and (tcp.clientport) of the response to get the full session.</p><p>Other way is just to click at the Reletatd Request in the Response Packet at Packet Detail Pane.</p><p>It is that what you mean? Or have you meant any different?</p></div><div id="comment-46743-info" class="comment-info"><span class="comment-age">(19 Oct '15, 21:43)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46756"></span><div id="comment-46756" class="comment"><div id="post-46756-score" class="comment-score"></div><div class="comment-text"><p>Packet Detail Pane does give the packet number of the matching request. Thanks for the tip. Ideally I would like all the desired requests and response show up in the packet list pane.</p></div><div id="comment-46756-info" class="comment-info"><span class="comment-age">(20 Oct '15, 07:21)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="46758"></span><div id="comment-46758" class="comment"><div id="post-46758-score" class="comment-score"></div><div class="comment-text"><p>Http is sequential protocol. There for the combination of client ip and client port will show you the req and resp for sure. But of course it could be that it shows you too much.</p></div><div id="comment-46758-info" class="comment-info"><span class="comment-age">(20 Oct '15, 07:25)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-46720" class="comment-tools"></div><div class="clear"></div><div id="comment-46720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46732"></span>

<div id="answer-container-46732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46732-score" class="post-score" title="current number of votes">0</div><span id="post-46732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>wonder if there is a way to extract the transactions</p></blockquote><p>well, please define 'extract'.</p><blockquote><p>whose response body starts with 3 characters "CWS" (Adobe flash).</p></blockquote><p>can you please try the following</p><blockquote><p>http.response and data-text-lines matches "^CWS"</p></blockquote><p>or case insensitive</p><blockquote><p>http.response and data-text-lines matches "^(?i)cws"</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46732" class="comments-container"><span id="46737"></span><div id="comment-46737" class="comment"><div id="post-46737-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@kurt</span>-knochner for the question. Clarification: "Extract" means filtering the packets in the pcap so that only the packets related to the desired HTTP transactions will remain, I can then save them to another (smaller) pcap. <code>http.response and data-text-lines matches "^CWS"</code> didn't catch it even though I saw the HTTP response body starts with it. See pcap <a href="https://www.cloudshark.org/captures/073d4570c609">https://www.cloudshark.org/captures/073d4570c609</a> (from malware-traffic-analysis.net) at packet 72.</p></div><div id="comment-46737-info" class="comment-info"><span class="comment-age">(19 Oct '15, 17:26)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="46747"></span><div id="comment-46747" class="comment"><div id="post-46747-score" class="comment-score"></div><div class="comment-text"><p>In your case, the best filter would be a 'media matches ...' as mentioned by <span>@Christian_R</span>, with a small change:</p><blockquote><p>media matches "^(?i)CWS"</p></blockquote><p>Then right click the frame and choose "Follow TCP Stream".</p></div><div id="comment-46747-info" class="comment-info"><span class="comment-age">(20 Oct '15, 00:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46757"></span><div id="comment-46757" class="comment"><div id="post-46757-score" class="comment-score"></div><div class="comment-text"><p>Yes <span>@kurt</span>-knochner, <code>media matches "^(?i)CWS"</code> works, thanks. Follow TCP stream works to a degree, I hope I would see all the desired requests and responses in the packet detailed pane.</p></div><div id="comment-46757-info" class="comment-info"><span class="comment-age">(20 Oct '15, 07:24)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-46732" class="comment-tools"></div><div class="clear"></div><div id="comment-46732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

