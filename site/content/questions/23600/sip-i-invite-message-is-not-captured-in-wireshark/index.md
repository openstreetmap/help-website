+++
type = "question"
title = "SIP-I INVITE message is not captured in Wireshark"
description = '''I&#x27;m trying to capture a SIP-I call using wireshark, i get all the messages except INVITE. Do you know why the INVITE is not captured? Is is due to MTU issue or something. We can see INVITE properly when we use pure SIP, issue happens to SIP-I INVITE only. Any help to sort this issue is highly apprec...'''
date = "2013-08-06T23:32:00Z"
lastmod = "2013-11-21T06:05:00Z"
weight = 23600
keywords = [ "sip" ]
aliases = [ "/questions/23600" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SIP-I INVITE message is not captured in Wireshark](/questions/23600/sip-i-invite-message-is-not-captured-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23600-score" class="post-score" title="current number of votes">0</div><span id="post-23600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture a SIP-I call using wireshark, i get all the messages except INVITE. Do you know why the INVITE is not captured? Is is due to MTU issue or something. We can see INVITE properly when we use pure SIP, issue happens to SIP-I INVITE only. Any help to sort this issue is highly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '13, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/39b05d720177eb3efea0b3dff73b10cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravindu&#39;s gravatar image" /><p><span>Ravindu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravindu has no accepted answers">0%</span></p></div></div><div id="comments-container-23600" class="comments-container"><span id="23612"></span><div id="comment-23612" class="comment"><div id="post-23612-score" class="comment-score"></div><div class="comment-text"><p>Have you checked that the problem isn't that Wireshark fails to recognise the message as SIP?</p></div><div id="comment-23612-info" class="comment-info"><span class="comment-age">(07 Aug '13, 08:33)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="23624"></span><div id="comment-23624" class="comment"><div id="post-23624-score" class="comment-score"></div><div class="comment-text"><p>Hello Anders, Thanks for your comment &amp; you are right. Seems wireshark can't identify it as SIP. Any idea how this can be solved?</p></div><div id="comment-23624-info" class="comment-info"><span class="comment-age">(07 Aug '13, 20:09)</span> <span class="comment-user userinfo">Ravindu</span></div></div><span id="26386"></span><div id="comment-26386" class="comment"><div id="post-26386-score" class="comment-score"></div><div class="comment-text"><p>Hello Anders, You are correct, INVITE is displayed until the IPV4 layer &amp; seems Wireshark can't identify it after that. I have uploaded a trace in the below link. Appreciate your help.</p><p><a href="http://www.cloudshark.org/captures/82506ab125bd">http://www.cloudshark.org/captures/82506ab125bd</a></p></div><div id="comment-26386-info" class="comment-info"><span class="comment-age">(24 Oct '13, 19:48)</span> <span class="comment-user userinfo">Ravindu</span></div></div><span id="26388"></span><div id="comment-26388" class="comment"><div id="post-26388-score" class="comment-score"></div><div class="comment-text"><p>It's a packet fragment (observe the fragment offset field in the inner IP header). Also the other fragment isn't in the trace file, explaining why it's not decoding as an IAM/INVITE.</p><p>Are you creating the capture file with an application-level display filter, such as "sip", or are you saving based on port number, IP, etc.? I'm wondering if the missing packet might have got lost due to Wireshark only displaying the last fragment as the actual SIP message, where the first packet wasn't caught in the display filter to be saved.</p></div><div id="comment-26388-info" class="comment-info"><span class="comment-age">(24 Oct '13, 20:08)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-23600" class="comment-tools"></div><div class="clear"></div><div id="comment-23600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23625"></span>

<div id="answer-container-23625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23625-score" class="post-score" title="current number of votes">0</div><span id="post-23625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well it could be a bug in Wireshark or the SIP header isn't formed according to the RFC(s) in witch case the sending application needs to be fixed. You could open up a bug report and let us have a look at the trace to try to determine which case it is or have a look at the code in packet-sip.c</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '13, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-23625" class="comments-container"><span id="26332"></span><div id="comment-26332" class="comment"><div id="post-26332-score" class="comment-score"></div><div class="comment-text"><p>I'm having the same issue.Regarding the trace required, How can I get the trace if I cant capture it?</p></div><div id="comment-26332-info" class="comment-info"><span class="comment-age">(23 Oct '13, 12:07)</span> <span class="comment-user userinfo">AshenC</span></div></div><span id="26335"></span><div id="comment-26335" class="comment"><div id="post-26335-score" class="comment-score"></div><div class="comment-text"><p>Well the presumtion is that the message <em>is</em> in the trace as UDP or TCP but for some reason Wireshark isn't interpreating it as SIP. With a trace we could perhaps determine if that's the case.</p></div><div id="comment-26335-info" class="comment-info"><span class="comment-age">(23 Oct '13, 13:23)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="26384"></span><div id="comment-26384" class="comment"><div id="post-26384-score" class="comment-score"></div><div class="comment-text"><p>Could you upload the capture file and post the link? <a href="http://www.cloudshark.org/">http://www.cloudshark.org/</a></p></div><div id="comment-26384-info" class="comment-info"><span class="comment-age">(24 Oct '13, 18:04)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="27207"></span><div id="comment-27207" class="comment"><div id="post-27207-score" class="comment-score"></div><div class="comment-text"><p>Just wondering if there was a resolution to this problem, I'm having the same problem with no sip invites, however my colleague's laptop seems to be fine. The only only difference is my laptop is 64bit win7 and his is 32bit win7.<br />
</p></div><div id="comment-27207-info" class="comment-info"><span class="comment-age">(21 Nov '13, 03:06)</span> <span class="comment-user userinfo">GTE01</span></div></div><span id="27214"></span><div id="comment-27214" class="comment"><div id="post-27214-score" class="comment-score"></div><div class="comment-text"><p>can you provide a capture file? The problem of <span>@Ravindu</span> was, that there were packets missing in the provided capture file.</p></div><div id="comment-27214-info" class="comment-info"><span class="comment-age">(21 Nov '13, 06:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-23625" class="comment-tools"></div><div class="clear"></div><div id="comment-23625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

