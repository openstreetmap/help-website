+++
type = "question"
title = "tcp previous segment not captured"
description = '''we have put in a new server and netgear 48 port switch where previously they had a hub, Internet access is working perfect and they get 60Mb to the desks, however an issue that has started that was ok before is that 1 application on 4 machines out of 7 is getting eggtiming and they are being kicked ...'''
date = "2016-03-29T09:30:00Z"
lastmod = "2016-04-01T06:32:00Z"
weight = 51260
keywords = [ "wire", "ask.wireshark.org", "wireshark" ]
aliases = [ "/questions/51260" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp previous segment not captured](/questions/51260/tcp-previous-segment-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51260-score" class="post-score" title="current number of votes">0</div><span id="post-51260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we have put in a new server and netgear 48 port switch where previously they had a hub, Internet access is working perfect and they get 60Mb to the desks, however an issue that has started that was ok before is that 1 application on 4 machines out of 7 is getting eggtiming and they are being kicked out of the app (inhouse application that runs mainly with FTP) this happens randomly but frequently and other apps do not seem affected.</p><p>At points the trace log to one of the machine is showing tcp previous segment not captured.</p><p>Could anyone help me interpret the packet capture, apologies as i have not used it before.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wire" rel="tag" title="see questions tagged &#39;wire&#39;">wire</span> <span class="post-tag tag-link-ask.wireshark.org" rel="tag" title="see questions tagged &#39;ask.wireshark.org&#39;">ask.wireshark.org</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '16, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/9ecccaa182f266f38704363c8ba8aa75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roadrunner123&#39;s gravatar image" /><p><span>Roadrunner123</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roadrunner123 has no accepted answers">0%</span></p></div></div><div id="comments-container-51260" class="comments-container"><span id="51261"></span><div id="comment-51261" class="comment"><div id="post-51261-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace at a public accessible place like: cloud shark or dropbox</p></div><div id="comment-51261-info" class="comment-info"><span class="comment-age">(29 Mar '16, 10:00)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="51280"></span><div id="comment-51280" class="comment"><div id="post-51280-score" class="comment-score"></div><div class="comment-text"><p>Here is a link to the capture i took yesterday</p><p><a href="https://www.dropbox.com/sh/d0882y2g9i1xux1/AABjl8fWEACj4-2huuMdSJ4Ha?dl=0">https://www.dropbox.com/sh/d0882y2g9i1xux1/AABjl8fWEACj4-2huuMdSJ4Ha?dl=0</a></p></div><div id="comment-51280-info" class="comment-info"><span class="comment-age">(30 Mar '16, 01:22)</span> <span class="comment-user userinfo">Roadrunner123</span></div></div><span id="51305"></span><div id="comment-51305" class="comment"><div id="post-51305-score" class="comment-score"></div><div class="comment-text"><p>Are we talking about FTP or are we talking about some filetransfers done by another protocol like SMB? Because I can´t see any FTP traffic in your trace.</p></div><div id="comment-51305-info" class="comment-info"><span class="comment-age">(30 Mar '16, 14:55)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="51309"></span><div id="comment-51309" class="comment"><div id="post-51309-score" class="comment-score"></div><div class="comment-text"><p>Thanks for commenting Christian, yes the propriatary software mainly uses FTP, i will run another trace this morning and upload it.</p></div><div id="comment-51309-info" class="comment-info"><span class="comment-age">(31 Mar '16, 01:09)</span> <span class="comment-user userinfo">Roadrunner123</span></div></div></div><div id="comment-tools-51260" class="comment-tools"></div><div class="clear"></div><div id="comment-51260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51284"></span>

<div id="answer-container-51284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51284-score" class="post-score" title="current number of votes">0</div><span id="post-51284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My interpretation is that</p><ol><li><p>the server application listening at port 8085 rejects several repeated attempts of 10.1.25.60 to connect; as the repeated attempts come from different ports and none of them succeeds, it does not seem to be caused by previous session using the same client side socket and closed shortly before. Some access rules at the server application are more likely. But I don't think it is a symptom of what you're after.</p></li><li><p>the "previous segment not captured" can be seen only once, in frame 1723, but it seems to be a symptom of some kind of larger network failure than of just a loss of a single frame and thus a better indicator of an issue. The last "fine" frame is 1719, then there are some 78 seconds of silence, and then the client (10.1.25.60) uses ARP to find out the MAC address of the server so that it could send the next frame. The last "fine" frame has a relative seq number of 3016, the "previous segment not captured" one has a relative seq number of 3056, so there should have been a 40-byte-payload packet in the same direction but it has not been captured.<br />
Soon after, the server sends again an ACK to 3016 so it has also not received that 40-byte-payload packet, i.e. it is not only an issue of capturing. This seems obvious here as the capture was running at the server itself, but I mention that as it would be an important indicator if the capture would be taken somewhere else along the network path between the client and the server.<br />
Does the client machine happen to have several network cards (including wireless), i.e. if the proper interface would be down, could it be that the missing packet would be sent via a different interface (and lost because it would not reach the destination as there is no network route between that other interface and the server)?<br />
As you wrote that you've replaced a hub by a switch, I would have a look at speed/duplex negotiation settings on the ports of the switch (and compare them between ports to which different client machines are connected), as it seems to me as if the client's network interface would be occasionally down at L1. And, still following the same idea, can you compare the network adaptor type and manufacturer of those 7 machines, maybe the 4 affected ones have a common make/model different from the remaining 3? Experience shows that "some" Ethernet adaptors have speed/duplex negotiation issues with "some" switches even if settings of both are compatible to each other.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '16, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-51284" class="comments-container"><span id="51285"></span><div id="comment-51285" class="comment"><div id="post-51285-score" class="comment-score"></div><div class="comment-text"><p>wow, thanks Sindy, the client machines are just average desktops with one network connection. i will have a look at the speed and duplex settings next and then the network adaptors.</p></div><div id="comment-51285-info" class="comment-info"><span class="comment-age">(30 Mar '16, 03:25)</span> <span class="comment-user userinfo">Roadrunner123</span></div></div><span id="51346"></span><div id="comment-51346" class="comment"><div id="post-51346-score" class="comment-score"></div><div class="comment-text"><p>One more point in completely different direction has come to my mind, can you capture <em>simultaneously</em> on the server and one of the problematic clients until you can see the issue happen? I'd like to be sure whether the client sends the missing frame (and so it got lost under way) or whether it does not send it at all. There could be issues like arp spoofing, causing the client to send it to a different MAC address, although it doesn't sound much likely as some client machines exhibit no problems when accessing the same server. But the issue is weird enough to look in all directions, and it is always useful to have a capture of the same occurrence of an issue from as many points along the path between the client and the server as possible.</p></div><div id="comment-51346-info" class="comment-info"><span class="comment-age">(01 Apr '16, 06:32)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-51284" class="comment-tools"></div><div class="clear"></div><div id="comment-51284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

