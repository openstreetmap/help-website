+++
type = "question"
title = "How to dissect USB network adapter traffic from USBpcap capture?"
description = '''I have done USBpcap capture, but I couldn&#x27;t make sense of the traffic capture because it doesn&#x27;t indicate the protocol type/s. Do you know how to interpret this raw capture? Thanks, Robert M.'''
date = "2016-12-19T11:54:00Z"
lastmod = "2016-12-19T12:22:00Z"
weight = 58235
keywords = [ "usbpcap" ]
aliases = [ "/questions/58235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect USB network adapter traffic from USBpcap capture?](/questions/58235/how-to-dissect-usb-network-adapter-traffic-from-usbpcap-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58235-score" class="post-score" title="current number of votes">0</div><span id="post-58235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have done USBpcap capture, but I couldn't make sense of the traffic capture because it doesn't indicate the protocol type/s. Do you know how to interpret this raw capture?</p><p>Thanks, Robert M.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usbpcap" rel="tag" title="see questions tagged &#39;usbpcap&#39;">usbpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '16, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/9717c2b8c36ec52a6855f4d6addb9d9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robertmi&#39;s gravatar image" /><p><span>robertmi</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robertmi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>19 Dec '16, 12:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-58235" class="comments-container"><span id="58236"></span><div id="comment-58236" class="comment"><div id="post-58236-score" class="comment-score"></div><div class="comment-text"><p>Wireshark would have to recognize the USB traffic to and from the network adapter as traffic to a network device <em>and</em> attempt to parse the traffic as network traffic. We'd have to see the capture to figure out why that's not happening.</p></div><div id="comment-58236-info" class="comment-info"><span class="comment-age">(19 Dec '16, 12:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-58235" class="comment-tools"></div><div class="clear"></div><div id="comment-58235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

