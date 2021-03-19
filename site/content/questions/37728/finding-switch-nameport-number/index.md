+++
type = "question"
title = "finding switch name/port number"
description = '''Hi, I need to find the switch info for a series of devices connected to a cisco switch. I have limited time in the suite, so I need to be able to plug into the jack the device uses, and ID the switch name, port number/ module number that the device is connecting to. Can I just to a CDP capture? I&#x27;ve...'''
date = "2014-11-10T07:26:00Z"
lastmod = "2014-11-12T14:09:00Z"
weight = 37728
keywords = [ "cdp", "cisco" ]
aliases = [ "/questions/37728" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [finding switch name/port number](/questions/37728/finding-switch-nameport-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37728-score" class="post-score" title="current number of votes">0</div><span id="post-37728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to find the switch info for a series of devices connected to a cisco switch. I have limited time in the suite, so I need to be able to plug into the jack the device uses, and ID the switch name, port number/ module number that the device is connecting to. Can I just to a CDP capture? I've tried but the I dont see the switch info.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cdp" rel="tag" title="see questions tagged &#39;cdp&#39;">cdp</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '14, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/c41fbfb6e54ce79b1ece53924d07f081?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wildbob&#39;s gravatar image" /><p><span>wildbob</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wildbob has no accepted answers">0%</span></p></div></div><div id="comments-container-37728" class="comments-container"><span id="37742"></span><div id="comment-37742" class="comment"><div id="post-37742-score" class="comment-score"></div><div class="comment-text"><p>Maybe I'm missing something, but can't you just pull the jack and make note of what port on the switch goes into a down/down state? Are you able to log into the switch?</p></div><div id="comment-37742-info" class="comment-info"><span class="comment-age">(10 Nov '14, 22:07)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-37728" class="comment-tools"></div><div class="clear"></div><div id="comment-37728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37729"></span>

<div id="answer-container-37729" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37729-score" class="post-score" title="current number of votes">0</div><span id="post-37729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you can try the show lldp nei</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '14, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/1ce4fe2b91a61d892d4c9b6a373704eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shlomig&#39;s gravatar image" /><p><span>shlomig</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shlomig has no accepted answers">0%</span></p></div></div><div id="comments-container-37729" class="comments-container"><span id="37731"></span><div id="comment-37731" class="comment"><div id="post-37731-score" class="comment-score"></div><div class="comment-text"><p>Upload a capture file with the CDP capture, and maybe someone can help you. You cannot upload directly to ask.wireshark.org, so upload your capture file somewhere and post a link to the file. A good choice is www.cloudshark.org. Dropbox or Google Drive will work as well.</p></div><div id="comment-37731-info" class="comment-info"><span class="comment-age">(10 Nov '14, 08:53)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="37737"></span><div id="comment-37737" class="comment"><div id="post-37737-score" class="comment-score"></div><div class="comment-text"><p>Yeah, I'm wondering if my Laptop Symantec AV/firewall wasn't letting CDP/lldp traffic through..</p></div><div id="comment-37737-info" class="comment-info"><span class="comment-age">(10 Nov '14, 12:18)</span> <span class="comment-user userinfo">wildbob</span></div></div><span id="37791"></span><div id="comment-37791" class="comment"><div id="post-37791-score" class="comment-score"></div><div class="comment-text"><p>Thanks folks, I ended up just having one of the folks from network eng search by my MAC address and IP, and find out where I was plugging into.. I couldn't log into the switch, and had to be in and out of these rooms (medical procedure rooms)as fast as possible</p></div><div id="comment-37791-info" class="comment-info"><span class="comment-age">(12 Nov '14, 06:50)</span> <span class="comment-user userinfo">wildbob</span></div></div><span id="37799"></span><div id="comment-37799" class="comment"><div id="post-37799-score" class="comment-score"></div><div class="comment-text"><p>With most managed switches you can either enable CDP or LLDP at the switch. But you will need to wait 30 seconds to 1 minute to see these being broadcasted. Just make sure you have Wireshark in promiscuous mode and no firewall on your capture device.</p></div><div id="comment-37799-info" class="comment-info"><span class="comment-age">(12 Nov '14, 14:09)</span> <span class="comment-user userinfo">martyvis</span></div></div></div><div id="comment-tools-37729" class="comment-tools"></div><div class="clear"></div><div id="comment-37729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

