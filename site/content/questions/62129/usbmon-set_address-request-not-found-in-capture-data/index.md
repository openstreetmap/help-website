+++
type = "question"
title = "usbmon Set_Address request not found in capture data"
description = '''hi, I was trying to analyze the communication with HID device(mouse) with wireshark. As per the protocol,in the enumeration process The host sends a Get_Descriptor request to device address 0, Endpoint 0 learn the maximum packet size of the default pipe. After this the host controller has to assigns...'''
date = "2017-06-19T10:13:00Z"
lastmod = "2017-06-19T12:54:00Z"
weight = 62129
keywords = [ "usbmon" ]
aliases = [ "/questions/62129" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [usbmon Set\_Address request not found in capture data](/questions/62129/usbmon-set_address-request-not-found-in-capture-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62129-score" class="post-score" title="current number of votes">0</div><span id="post-62129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I was trying to analyze the communication with HID device(mouse) with wireshark. As per the protocol,in the enumeration process The host sends a Get_Descriptor request to device address 0, Endpoint 0 learn the maximum packet size of the default pipe. After this the host controller has to assigns a unique address to the device by sending a Set_Address request. But in the captured data there is no Set_Address request even though the communication is happening with a different address. why is it so?? please help. Please check the attached capture file <a href="https://www.dropbox.com/s/uy67auanq5qdx5q/USB%20Mouse.pcapng?dl=0">https://www.dropbox.com/s/uy67auanq5qdx5q/USB%20Mouse.pcapng?dl=0</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usbmon" rel="tag" title="see questions tagged &#39;usbmon&#39;">usbmon</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '17, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/56cb43cd1e133d5f5bdd455afcbf3478?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gladiator&#39;s gravatar image" /><p><span>gladiator</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gladiator has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jun '17, 21:16</strong> </span></p></div></div><div id="comments-container-62129" class="comments-container"><span id="62135"></span><div id="comment-62135" class="comment"><div id="post-62135-score" class="comment-score"></div><div class="comment-text"><p>Do not post screenshots, post the capture files - either at cloudshark or at any file sharing service, and edit your question with a link to the file. Analyse of screenshots is close to impossible.</p></div><div id="comment-62135-info" class="comment-info"><span class="comment-age">(19 Jun '17, 12:54)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62129" class="comment-tools"></div><div class="clear"></div><div id="comment-62129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

