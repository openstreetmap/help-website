+++
type = "question"
title = "Dissect http traffic on a non-standard port"
description = '''I have a trace file that has http traffic on port 87, even though I add port 87 to http protocol preferences settings and I also tried &quot;decoded as&quot;, but still it does not display &quot;source/ destination port = 87&quot; or &quot;http&quot; in the info column. Any suggestions from the experts! '''
date = "2014-07-31T16:56:00Z"
lastmod = "2015-05-13T17:38:00Z"
weight = 35038
keywords = [ "http" ]
aliases = [ "/questions/35038" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dissect http traffic on a non-standard port](/questions/35038/dissect-http-traffic-on-a-non-standard-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35038-score" class="post-score" title="current number of votes">0</div><span id="post-35038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace file that has http traffic on port 87, even though I add port 87 to http protocol preferences settings and I also tried "decoded as", but still it does not display "source/ destination port = 87" or "http" in the info column. Any suggestions from the experts!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '14, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/9ee914a9fba57513c2612c9d2735a862?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyverzek&#39;s gravatar image" /><p><span>cyverzek</span><br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyverzek has no accepted answers">0%</span></p></div></div><div id="comments-container-35038" class="comments-container"><span id="35043"></span><div id="comment-35043" class="comment"><div id="post-35043-score" class="comment-score">1</div><div class="comment-text"><p>what is your</p><ul><li>Wireshark release</li><li>OS and OS version</li></ul><p>Can you please</p><ul><li>post a sample capture file somewhere (google drive, dropbox, cloudshark.org)</li></ul></div><div id="comment-35043-info" class="comment-info"><span class="comment-age">(01 Aug '14, 00:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35108"></span><div id="comment-35108" class="comment"><div id="post-35108-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.8.3 BT 3.2.6</p><p>The trace file is available at <a href="http://www.wiresharkbook.com/101_supplements/wireshark101files.zip.">http://www.wiresharkbook.com/101_supplements/wireshark101files.zip.</a> It's name is challenge101-1.pcapng</p></div><div id="comment-35108-info" class="comment-info"><span class="comment-age">(03 Aug '14, 10:27)</span> <span class="comment-user userinfo">cyverzek</span></div></div><span id="35109"></span><div id="comment-35109" class="comment"><div id="post-35109-score" class="comment-score"></div><div class="comment-text"><p>what is <strong>BT 3.2.6</strong> ? That does not sound like a standard version of Wireshark.</p></div><div id="comment-35109-info" class="comment-info"><span class="comment-age">(03 Aug '14, 10:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35121"></span><div id="comment-35121" class="comment"><div id="post-35121-score" class="comment-score"></div><div class="comment-text"><p>OS BackTrack 5.3 and kernel 3.2.6, sorry for the confusion.</p></div><div id="comment-35121-info" class="comment-info"><span class="comment-age">(03 Aug '14, 12:37)</span> <span class="comment-user userinfo">cyverzek</span></div></div><span id="37279"></span><div id="comment-37279" class="comment"><div id="post-37279-score" class="comment-score"></div><div class="comment-text"><p>I am using 1.12.1 on Windows 7 and having the same problem? I am using the example from Wireshark 101 (Challenge101.pcapng)</p><p>Have tried both methods (decode as and adding port to http dissector), nothing is working.</p></div><div id="comment-37279-info" class="comment-info"><span class="comment-age">(22 Oct '14, 06:37)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="37288"></span><div id="comment-37288" class="comment not_top_scorer"><div id="post-37288-score" class="comment-score"></div><div class="comment-text"><p>There is nothing special you'll have to do. Wireshark detects HTTP on port 87 "automagically". Anyway, even if it would not detect it, the "Decode As" feature should work. I tested it with the mentioned capture file. Here are my results (Wireshark 1.12.1 / Win7 - <strong>no change at all</strong>).</p><p><img src="https://osqa-ask.wireshark.org/upfiles/http_on_port_87_2KDi7bY.png" alt="alt text" /></p><p>If your problem persist, please open your own question, as the OP was using a different Wireshark version and OS!</p></div><div id="comment-37288-info" class="comment-info"><span class="comment-age">(22 Oct '14, 08:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35038" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-35038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35122"></span>

<div id="answer-container-35122" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35122-score" class="post-score" title="current number of votes">1</div><span id="post-35122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Although "Decode as" should work with 1.8.3, can you please try <a href="http://www.kali.org/">Kali Linux</a>, the successor of BackTrack? It provides a newer release of Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '14, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-35122" class="comments-container"></div><div id="comment-tools-35122" class="comment-tools"></div><div class="clear"></div><div id="comment-35122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42381"></span>

<div id="answer-container-42381" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42381-score" class="post-score" title="current number of votes">0</div><span id="post-42381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you can try to right click on the frame and under protocol preferences verify that "Allow subdissector to reassemble TCP streams" is checked</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 17:38</strong></p><img src="https://secure.gravatar.com/avatar/eda96ad10feffdbe22faa88ad508d969?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johannes&#39;s gravatar image" /><p><span>johannes</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johannes has no accepted answers">0%</span></p></div></div><div id="comments-container-42381" class="comments-container"></div><div id="comment-tools-42381" class="comment-tools"></div><div class="clear"></div><div id="comment-42381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

