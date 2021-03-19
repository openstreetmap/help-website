+++
type = "question"
title = "wireshark settings"
description = '''Now I am working with wireshark and facing some problems. I want to communicate two ieds with my pc &amp;amp; want to see the communication between the two ieds. plz tell me the settings which are to be set to see the packets. ieds ip(for client-192.168.0.105,,,for slave-192.168.0.24,,,pc-192.168.0.162)...'''
date = "2013-06-19T02:55:00Z"
lastmod = "2013-06-19T10:24:00Z"
weight = 22149
keywords = [ "settings", "wireshark" ]
aliases = [ "/questions/22149" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark settings](/questions/22149/wireshark-settings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22149-score" class="post-score" title="current number of votes">0</div><span id="post-22149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Now I am working with wireshark and facing some problems. I want to communicate two ieds with my pc &amp; want to see the communication between the two ieds. plz tell me the settings which are to be set to see the packets. ieds ip(for client-192.168.0.105,,,for slave-192.168.0.24,,,pc-192.168.0.162)...plz rply me fast,,,,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-settings" rel="tag" title="see questions tagged &#39;settings&#39;">settings</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '13, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/fe0041b25a159fef5704fafee3a87e52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nayan&#39;s gravatar image" /><p><span>nayan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nayan has no accepted answers">0%</span></p></div></div><div id="comments-container-22149" class="comments-container"><span id="22150"></span><div id="comment-22150" class="comment"><div id="post-22150-score" class="comment-score"></div><div class="comment-text"><p>what are ieds?</p></div><div id="comment-22150-info" class="comment-info"><span class="comment-age">(19 Jun '13, 02:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22158"></span><div id="comment-22158" class="comment"><div id="post-22158-score" class="comment-score"></div><div class="comment-text"><p>I was thinking "improvised explosive device" when I saw that text... I wouldn't call it "improvised" anymore if a device like that talks via IP, so I guess that is not what it is :-)</p></div><div id="comment-22158-info" class="comment-info"><span class="comment-age">(19 Jun '13, 07:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="22162"></span><div id="comment-22162" class="comment"><div id="post-22162-score" class="comment-score"></div><div class="comment-text"><p>Yeah, that was the first thing I found with google ;-))</p><blockquote><p>I wouldn't call it "improvised"</p></blockquote><p>Maybe it's an <strong>improved</strong> explosive device.</p></div><div id="comment-22162-info" class="comment-info"><span class="comment-age">(19 Jun '13, 07:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22178"></span><div id="comment-22178" class="comment"><div id="post-22178-score" class="comment-score"></div><div class="comment-text"><p>An IED can also be an Intelligent Electronic Device, another name for a PLC or RTU, often used in the electrical distribution industry.</p><p>The devices aren't all that intelligent really but compared to all the other devices in the electrical distribution network they're like super computers.</p></div><div id="comment-22178-info" class="comment-info"><span class="comment-age">(19 Jun '13, 10:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-22149" class="comment-tools"></div><div class="clear"></div><div id="comment-22149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22179"></span>

<div id="answer-container-22179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22179-score" class="post-score" title="current number of votes">0</div><span id="post-22179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How you capture depends on your network architecture. Presumably the IED's and the PC are plugged into a switch, so you'll need to get the switch to span or mirror the traffic between the IED's to the port for the PC.</p><p>See the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '13, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22179" class="comments-container"></div><div id="comment-tools-22179" class="comment-tools"></div><div class="clear"></div><div id="comment-22179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

