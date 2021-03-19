+++
type = "question"
title = "how to check content of only one frame in the follow tcp stream window"
description = '''Hello, I need to see changes that are done by a cisco asa after sip inspection. I can see that incomming tcp segment is 1452 bytes. Living the asa it&#x27;s already 1460 bytes. The changes are made on application level. To see the stream content on the layer 7 I choose a frame from that tcp stream and cl...'''
date = "2016-03-03T08:23:00Z"
lastmod = "2016-03-04T02:17:00Z"
weight = 50704
keywords = [ "followtcpstream" ]
aliases = [ "/questions/50704" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to check content of only one frame in the follow tcp stream window](/questions/50704/how-to-check-content-of-only-one-frame-in-the-follow-tcp-stream-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50704-score" class="post-score" title="current number of votes">0</div><span id="post-50704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to see changes that are done by a cisco asa after sip inspection. I can see that incomming tcp segment is 1452 bytes. Living the asa it's already 1460 bytes. The changes are made on application level. To see the stream content on the layer 7 I choose a frame from that tcp stream and click on follow TCP stream. Now I can see an ASCII Text for entire conversation in this tcp stream. If I click on an text entry, the corresponded frame is highlighted in the wireshark. Click on an other part of the text, an other frame is highlighted. It happens the text entries that belong to one frame are spread over the entire follow tcp stream ASCII text. What I need is to see or highlight the layer 7 (ASCII text) information only for one frame in the tcp stream. Is it possible? Thanks Sergej</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-followtcpstream" rel="tag" title="see questions tagged &#39;followtcpstream&#39;">followtcpstream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '16, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/bb062fbb428215811dc67ca997cc44a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seb&#39;s gravatar image" /><p><span>seb</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Mar '16, 09:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-50704" class="comments-container"></div><div id="comment-tools-50704" class="comment-tools"></div><div class="clear"></div><div id="comment-50704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50712"></span>

<div id="answer-container-50712" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50712-score" class="post-score" title="current number of votes">2</div><span id="post-50712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can select a single frame in the packet (frame) list, either by clicking it directly in the packet list pane of the basic Wireshark window or by clicking the corresponding part of text in the "follow tcp stream" window, and then look into the packet dissection pane in the basic window. There you should have two "cards", one showing only the payload of that tcp packet alone and the other showing reassembled data from multiple tcp packets - in this case, the whole SIP message whose part is in the selected frame.</p><p>I don't have the details of your scenario, but I assume that you want to see the modification performed by the ASA. To do so, you would right-click the line "Session Initiation Protocol - SIP" in the packet dissection tree in the packet dissection pane and choose <code>Copy -&gt; ...as Printable Text</code> and then paste the contents of the clipboard into a text editor. You would do this for both messages (the original one and the one mangled by ASA) and compare them using your eyes or <code>diff</code>.</p><p>If it does not work for you, please publish the capture and provide a link to it, I haven't found any SIP over TCP capture in my archive so I could not check each step of my description.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '16, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50712" class="comments-container"><span id="50716"></span><div id="comment-50716" class="comment"><div id="post-50716-score" class="comment-score"></div><div class="comment-text"><p>Thanks, sindy. It works.</p></div><div id="comment-50716-info" class="comment-info"><span class="comment-age">(04 Mar '16, 02:17)</span> <span class="comment-user userinfo">seb</span></div></div></div><div id="comment-tools-50712" class="comment-tools"></div><div class="clear"></div><div id="comment-50712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

