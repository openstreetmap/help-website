+++
type = "question"
title = "Packet annotation / comments - v1.10.2 - Not Working"
description = '''I am running Wireshark 1.10.2 on Windows 7 and have found a problem. This happens on two different computers running those versions.  When I place an annotation on any packet - that comment is on every packet. If I edit the comment on one packet, it is edited in all the others.  For example: If I cl...'''
date = "2013-10-26T10:27:00Z"
lastmod = "2013-10-27T17:51:00Z"
weight = 26424
keywords = [ "pcapng", "annotation", "wireshark" ]
aliases = [ "/questions/26424" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet annotation / comments - v1.10.2 - Not Working](/questions/26424/packet-annotation-comments-v1102-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26424-score" class="post-score" title="current number of votes">0</div><span id="post-26424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark 1.10.2 on Windows 7 and have found a problem. This happens on two different computers running those versions.<br />
</p><p>When I place an annotation on any packet - that comment is on every packet. If I edit the comment on one packet, it is edited in all the others.<br />
</p><p>For example: If I click on packet #3 and add the annotation "comment on packet 3".</p><p>Then select packet #6, it has an annotation of "comment on packet 3". If I edit that annotation to say "comment on packet 6", and go back to packet 3, it now has the "comment on packet 6" annotation.</p><p>BTW... whatever the current comment on packets - going into Statistics | Summary shows that comment and editing it there changes it on all packets.</p><p>Has anyone else seen this behavior?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-annotation" rel="tag" title="see questions tagged &#39;annotation&#39;">annotation</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '13, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/eb859ad26d92eb0902b45ba20a167917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kpalmgren&#39;s gravatar image" /><p><span>kpalmgren</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kpalmgren has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-26424" class="comments-container"></div><div id="comment-tools-26424" class="comment-tools"></div><div class="clear"></div><div id="comment-26424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26425"></span>

<div id="answer-container-26425" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26425-score" class="post-score" title="current number of votes">0</div><span id="post-26425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, I can confirm this behavior on 1.10.2 as well as on the trunk. Another problem is that the packet comments are not listed in the Expert Infos tab. Please file a bug report.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '13, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-26425" class="comments-container"><span id="26426"></span><div id="comment-26426" class="comment"><div id="post-26426-score" class="comment-score"></div><div class="comment-text"><p>Bug Report <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9331">#9331</a> submitted...</p></div><div id="comment-26426-info" class="comment-info"><span class="comment-age">(26 Oct '13, 11:55)</span> <span class="comment-user userinfo">kpalmgren</span></div></div><span id="26437"></span><div id="comment-26437" class="comment"><div id="post-26437-score" class="comment-score"></div><div class="comment-text"><p>Actually not a bug at all... the button in the lower left I was using is the button to place a comment for the entire file - the same comment as in the Statistics | Summary screen.</p><p>To comment on individual packets, right-click the packet and choose "Packet Comment"</p></div><div id="comment-26437-info" class="comment-info"><span class="comment-age">(27 Oct '13, 07:09)</span> <span class="comment-user userinfo">kpalmgren</span></div></div><span id="26448"></span><div id="comment-26448" class="comment"><div id="post-26448-score" class="comment-score"></div><div class="comment-text"><p>Well I guess you can tell how often I use packet comments. That seemed like the more intuitive way to add/edit comments to me than right-clicking.</p><p>Personally, I'd like to see some sort of icon/indicator in the packet list for each packet with a comment. I know if you click on a packet and it has a packet comment, the packet details will indicate this, and I realize that the Expert Infos will also list all packets with comments, but I think it'd still be nice not to have to rely on Expert Infos as the only way to be able to figure out which packets have comments and which don't.</p></div><div id="comment-26448-info" class="comment-info"><span class="comment-age">(27 Oct '13, 17:51)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-26425" class="comment-tools"></div><div class="clear"></div><div id="comment-26425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

