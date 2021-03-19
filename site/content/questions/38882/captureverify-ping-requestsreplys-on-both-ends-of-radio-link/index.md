+++
type = "question"
title = "Capture/Verify Ping Requests/Replys On Both Ends Of Radio Link?"
description = '''IP Camera setup with a server and one cam at location A and four additional cams at location B with the two locations joined via a radio link that is, AFIK, effectively a half-mile-long Ethernet cable. viz: http://tinyurl.com/mkfmvcx Every once-in-awhile, three of the cams at location B become unava...'''
date = "2015-01-04T13:37:00Z"
lastmod = "2015-01-04T16:41:00Z"
weight = 38882
keywords = [ "ping" ]
aliases = [ "/questions/38882" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Capture/Verify Ping Requests/Replys On Both Ends Of Radio Link?](/questions/38882/captureverify-ping-requestsreplys-on-both-ends-of-radio-link)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38882-score" class="post-score" title="current number of votes">0</div><span id="post-38882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>IP Camera setup with a server and one cam at location A and four additional cams at location B with the two locations joined via a radio link that is, AFIK, effectively a half-mile-long Ethernet cable. viz: <a href="http://tinyurl.com/mkfmvcx">http://tinyurl.com/mkfmvcx</a></p><p>Every once-in-awhile, three of the cams at location B become unavailable to the server at location A. Pinging shows groups of replies interspaced with Timeouts and Unreachables. viz: <a href="http://tinyurl.com/ouqrd95">http://tinyurl.com/ouqrd95</a></p><p>We have a PC at the remote location B and WireShark is installed on that PC and on the camera server PC at location A.</p><p>IP addr of Location A cam server is 10.0.0.33. IP addr of problem cam at Location B is 10.0.0.145.</p><p>Next time this happens, I would like to start up a Ping -t and see if the requests are getting from Location A to Location B at the moments of Timeouts and Unreachables.<br />
</p><p>Hopefully this will tell me something about whether the problem is in the radio link (which it probably is, since rebooting the radios makes the problem go away) or maybe in some combination of link/camera/something else that I cannot imagine.</p><p>So, <strong>The Question:</strong></p><p>How do I configure WireShark on each end to do this?<br />
</p><p>I think I have it for the server end (Location A, where the Pings are coming from):</p><ul><li><p>Fire up WireShark</p></li><li><p>Let it run for awhile</p></li><li><p>Quit and save a .cap file</p></li><li><p>Open said .cap file and apply the filter <em>(ip.src == 10.0.0.33 &amp;&amp; ip.dst==10.0.0.145) or (ip.src==10.0.0.145 &amp;&amp; ip.dst==10.0.0.33)</em></p></li></ul><p>But what to do at the other end (Location B)? The strategy just mentioned does not seem to work. Specifically, I cannot find any line items with Protocol=IMCP. IMCPV6, yes, but no plain old IMCP - which all the Requests/Replys are in the .cap at Location A.</p><p>FWIW: 64-bit WireShark at Location A, 32-bit WireShark at location B.</p><p>Also, it seems like I would have to determine what the unique ID for packets is so that, once I figure out the filter for Location B, I can check to see if a specific packet made it from Location A to Location B.</p><p>Does any of this make sense?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '15, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/8bde5a113e61480e8111dcc2e49409f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeteCress&#39;s gravatar image" /><p><span>PeteCress</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeteCress has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jan '15, 14:53</strong> </span></p></div></div><div id="comments-container-38882" class="comments-container"></div><div id="comment-tools-38882" class="comment-tools"></div><div class="clear"></div><div id="comment-38882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38886"></span>

<div id="answer-container-38886" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38886-score" class="post-score" title="current number of votes">0</div><span id="post-38886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="PeteCress has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At location B, you have Wireshark installed on a troubleshooting PC, but you're pinging the cameras. Everything is connected to a switch, so pings addressed to the camera at 10.0.0.145 are only going to go out the switch port that 10.0.0.145 is connected to. The ping packets will not be sent out the switch port that your Wireshark machine is connected to. See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">this Wiki page</a> for a discussion of capturing on an Ethernet switched network. The simplest solution is to see if your switch is capable of doing port mirroring. If so, set up port mirroring so that one of the camera ports is mirrored to the port where your Wireshark machine is connected and then ping that camera. You could also try pinging the troubleshooting PC directly, just to see if pings are making it across the wireless link.</p><p>You can simplify your filter to <em>ip.addr==10.0.0.33 &amp;&amp; ip.addr==10.0.0.145</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '15, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-38886" class="comments-container"><span id="38887"></span><div id="comment-38887" class="comment"><div id="post-38887-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the clear explaination.</p></div><div id="comment-38887-info" class="comment-info"><span class="comment-age">(04 Jan '15, 16:41)</span> <span class="comment-user userinfo">PeteCress</span></div></div></div><div id="comment-tools-38886" class="comment-tools"></div><div class="clear"></div><div id="comment-38886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

