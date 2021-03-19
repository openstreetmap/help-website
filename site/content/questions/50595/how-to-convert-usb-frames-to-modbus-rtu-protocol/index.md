+++
type = "question"
title = "How to Convert USB frames to Modbus RTU protocol"
description = '''Dear Sirs, I&#x27;m capturing frames of Modbus RTU protocol through a RS485/USB converter using USBPcap plugin. The problem is that I want to see the frames in Modbus RTU protocol because it appears as USB encapsulated. Is it possible to change the protocol/encapsulated from USB to Modbus RTU? How? Thank...'''
date = "2016-03-01T00:10:00Z"
lastmod = "2016-03-01T03:29:00Z"
weight = 50595
keywords = [ "usbpcap" ]
aliases = [ "/questions/50595" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to Convert USB frames to Modbus RTU protocol](/questions/50595/how-to-convert-usb-frames-to-modbus-rtu-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50595-score" class="post-score" title="current number of votes">0</div><span id="post-50595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Image1_mSPUBuq.jpg" alt="alt text" /><img src="https://osqa-ask.wireshark.org/upfiles/Image2.jpg" alt="alt text" />Dear Sirs,</p><p>I'm capturing frames of Modbus RTU protocol through a RS485/USB converter using USBPcap plugin. The problem is that I want to see the frames in Modbus RTU protocol because it appears as USB encapsulated. Is it possible to change the protocol/encapsulated from USB to Modbus RTU? How?</p><p>Thank you in advanced</p><p>Regards,</p><p>Julio</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usbpcap" rel="tag" title="see questions tagged &#39;usbpcap&#39;">usbpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '16, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/759fa9d6a76b2a60fdfe6624dff6d730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JCada&#39;s gravatar image" /><p><span>JCada</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JCada has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Mar '16, 00:19</strong> </span></p></div></div><div id="comments-container-50595" class="comments-container"><span id="50597"></span><div id="comment-50597" class="comment"><div id="post-50597-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc.?</p></div><div id="comment-50597-info" class="comment-info"><span class="comment-age">(01 Mar '16, 02:01)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="50600"></span><div id="comment-50600" class="comment"><div id="post-50600-score" class="comment-score"></div><div class="comment-text"><p><span>@JCada</span>, let me draw your attention to the fact that USB dissectors may need to "see" the enumeration phase in order to choose the proper sub-dissector for the (otherwise pretty generic) USB frame contents - in this case, the data must be dissected as serial communication over the prolific chip, which in turn may be dissected as Modbus RTU. I do not promise it will work, but try to capture the following way:</p><ol><li><p>stop the Modbus control application and gracefully unplug the USB Modbus adaptor</p></li><li><p>start capturing on the relevant root hub (#2 in your case)</p></li><li><p>plug the USB Modbus adaptor back to the same socket where it was before</p></li><li><p>start the Modbus control application and capture the issue you are interested in</p></li><li><p>stop the capture</p></li><li><p>see whether it has helped</p></li><li><p>if not, save and publish the capture as <span>@grahamb</span> has suggested, otherwise there is little chance you could get more help unless someone has exactly the same experience and has managed to solve it in the past.</p></li></ol></div><div id="comment-50600-info" class="comment-info"><span class="comment-age">(01 Mar '16, 03:29)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50595" class="comment-tools"></div><div class="clear"></div><div id="comment-50595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

