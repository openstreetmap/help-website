+++
type = "question"
title = "calling a dissector fails with tvb subset in lua"
description = '''Hi,  I have an disssector that calls another post-dissector. That works fine in Wireshark 2.2.0 with  function my_proto.dissector(tvb,pinfo,tree)  local ptp_dissector_table = DissectorTable.get(&quot;ptp.data&quot;)  local packet_dissector = ptp_dissector_table:get_dissector(&#x27;ptp&#x27;)   packet_dissector(tvb, pin...'''
date = "2016-10-21T04:52:00Z"
lastmod = "2016-10-21T07:54:00Z"
weight = 56560
keywords = [ "lua", "subdissector", "tvb" ]
aliases = [ "/questions/56560" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [calling a dissector fails with tvb subset in lua](/questions/56560/calling-a-dissector-fails-with-tvb-subset-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56560-score" class="post-score" title="current number of votes">1</div><span id="post-56560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have an disssector that calls another post-dissector.</p><p>That works fine in Wireshark 2.2.0 with</p><pre><code>function my_proto.dissector(tvb,pinfo,tree)
    local ptp_dissector_table = DissectorTable.get(&quot;ptp.data&quot;)
    local packet_dissector = ptp_dissector_table:get_dissector(&#39;ptp&#39;) 
    packet_dissector(tvb, pinfo, tree) 
 end</code></pre><p>but fails as soon as I use</p><pre><code>  packet_dissector(tvb(some_offset), pinfo, tree)</code></pre><p>with 'Bad argument #2 to packet_dissector (Tvb expected, got userdata)</p><p>Any hints?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-subdissector" rel="tag" title="see questions tagged &#39;subdissector&#39;">subdissector</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '16, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/4875dbde2eebdc54b43edef7b9c29473?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20E&#39;s gravatar image" /><p><span>Thomas E</span><br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas E has no accepted answers">0%</span></p></div></div><div id="comments-container-56560" class="comments-container"></div><div id="comment-tools-56560" class="comment-tools"></div><div class="clear"></div><div id="comment-56560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56561"></span>

<div id="answer-container-56561" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56561-score" class="post-score" title="current number of votes">2</div><span id="post-56561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Thomas E has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use</p><pre><code>packet_dissector(tvb:range(some_offset,some_length):tvb(), pinfo, tree)</code></pre><p>(fixed according to the comment of <span><span>@Thomas E</span></span>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '16, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Oct '16, 10:46</strong> </span></p></div></div><div id="comments-container-56561" class="comments-container"><span id="56569"></span><div id="comment-56569" class="comment"><div id="post-56569-score" class="comment-score"></div><div class="comment-text"><p>Actually it is</p><p>packet_dissector(tvb:range(some_offset,some_length):tvb(), pinfo, tree)</p><p>Thanks, Thomas</p></div><div id="comment-56569-info" class="comment-info"><span class="comment-age">(21 Oct '16, 07:54)</span> <span class="comment-user userinfo">Thomas E</span></div></div></div><div id="comment-tools-56561" class="comment-tools"></div><div class="clear"></div><div id="comment-56561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

