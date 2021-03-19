+++
type = "question"
title = "Does Wireshark2.2.4 decode USB Audio Feature Unit Descriptor correctly?"
description = '''Hi All, I&#x27;m using wShark v2.2.4 on Win10 to capture USB Audio Traffic. However, I find the feature descriptor bmaControls (listed as &quot;Controls&quot; in wShark) value (0x010002) doesn&#x27;t match the breakdown bitset list of 0x0100, here bControlSize (&quot;ControlSize&quot; in wShark) is decoded as 2, and NrChannels (...'''
date = "2017-03-11T23:04:00Z"
lastmod = "2017-03-11T23:04:00Z"
weight = 60012
keywords = [ "audio", "usb" ]
aliases = [ "/questions/60012" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark2.2.4 decode USB Audio Feature Unit Descriptor correctly?](/questions/60012/does-wireshark224-decode-usb-audio-feature-unit-descriptor-correctly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60012-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I'm using wShark v2.2.4 on Win10 to capture USB Audio Traffic. However, I find the feature descriptor bmaControls (listed as "Controls" in wShark) value (0x010002) doesn't match the breakdown bitset list of 0x0100, here bControlSize ("ControlSize" in wShark) is decoded as 2, and NrChannels (in Input Terminal Descriptor) is 2. The remaining 0x02 doesn't have a reasonable explanation.</p><p>Can you help? If there is anything wrong in my question please let me know.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">audio usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '17, 23:04</strong></p><img src="https://secure.gravatar.com/avatar/45304f349d18e88ae1ab87c74747a8b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stndfir&#39;s gravatar image" /><p>stndfir<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stndfir has no accepted answers">0%</span></p></div></div><div id="comments-container-60012" class="comments-container"><span id="60015"></span><div id="comment-60015" class="comment"><div id="post-60015-score" class="comment-score"></div><div class="comment-text"><p>Capture file or it didn't happen.</p></div><div id="comment-60015-info" class="comment-info"><span class="comment-age">(12 Mar '17, 10:23)</span> Jaap ♦</div></div><span id="60016"></span><div id="comment-60016" class="comment"><div id="post-60016-score" class="comment-score"></div><div class="comment-text"><p>Should I know how to upload a .pcapng file to the thread here?</p></div><div id="comment-60016-info" class="comment-info"><span class="comment-age">(12 Mar '17, 12:22)</span> stndfir</div></div><span id="60017"></span><div id="comment-60017" class="comment"><div id="post-60017-score" class="comment-score"></div><div class="comment-text"><p>It is a cap file for Elite Portable USB Speaker I bought in Walmart.</p></div><div id="comment-60017-info" class="comment-info"><span class="comment-age">(12 Mar '17, 12:23)</span> stndfir</div></div><span id="60042"></span><div id="comment-60042" class="comment"><div id="post-60042-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>? There's no attaching capture files here.</p></div><div id="comment-60042-info" class="comment-info"><span class="comment-age">(13 Mar '17, 12:15)</span> Jaap ♦</div></div><span id="60070"></span><div id="comment-60070" class="comment"><div id="post-60070-score" class="comment-score"></div><div class="comment-text"><p>The cap file has been uploaded to CloudShark at <a href="https://www.cloudshark.org/captures/7100f776bdfd">https://www.cloudshark.org/captures/7100f776bdfd</a></p></div><div id="comment-60070-info" class="comment-info"><span class="comment-age">(14 Mar '17, 10:20)</span> stndfir</div></div><span id="60085"></span><div id="comment-60085" class="comment not_top_scorer"><div id="post-60085-score" class="comment-score"></div><div class="comment-text"><p>Packet #95 is the one with Feature Unit Descriptor. Any comment?</p></div><div id="comment-60085-info" class="comment-info"><span class="comment-age">(15 Mar '17, 04:34)</span> stndfir</div></div></div><div id="comment-tools-60012" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-60012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

