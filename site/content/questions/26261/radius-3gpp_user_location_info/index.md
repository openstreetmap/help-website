+++
type = "question"
title = "radius 3GPP_User_Location_Info"
description = '''Hello Guys, I am trying to extract 3GPP_User_Location_Info from Radius messages. However in this instance it is not extracting info correctly  $ tshark -v TShark 1.10.2 (SVN Rev 51934 from /trunk-1.10) tshark -T fields -e radius.Calling_Station_Id -e radius.3GPP_User_Location_Info -e radius.3GPP_IME...'''
date = "2013-10-21T15:34:00Z"
lastmod = "2013-10-21T16:59:00Z"
weight = 26261
keywords = [ "radius", "avp" ]
aliases = [ "/questions/26261" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [radius 3GPP\_User\_Location\_Info](/questions/26261/radius-3gpp_user_location_info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26261-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Guys,</p><p>I am trying to extract 3GPP_User_Location_Info from Radius messages. However in this instance it is not extracting info correctly</p><p>$ tshark -v TShark 1.10.2 (SVN Rev 51934 from /trunk-1.10)</p><p>tshark -T fields -e radius.Calling_Station_Id -e radius.3GPP_User_Location_Info -e radius.3GPP_IMEISV -e radius.Framed-IP-Address -E header=y -E separator=, -E quote=d -r Nikola_TEST_cap.pcap | head</p><p>radius.Calling_Station_Id,radius.3GPP_User_Location_Info,radius.3GPP_IMEISV,radius.Framed-IP-Address "6149891xxxx",,"3598220413753808","144.131.70.63" "6145563xxxx",,"3598220423540908","101.175.33.128"</p><p>For some reason the 3GPP-User-Location-Id AVP doesn’t get extracted by tshark, although Wireshark shows/decodes the AVP just file.</p><p>I upgraded my copy of Wireshark on the Mac to the latest but still seeing the same issue. The AVP is listed in the dictionary and in tshark –G fields so suspect it may be a bug? Other 3GPP fields are extracted ok.</p></div><div id="question-tags" class="tags-container tags">radius avp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '13, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/21d3400ec1fa515cfde9d6fb3027ce19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nik_NSW_2150&#39;s gravatar image" /><p>Nik_NSW_2150<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nik_NSW_2150 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '13, 17:03</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-26261" class="comments-container"></div><div id="comment-tools-26261" class="comment-tools"></div><div class="clear"></div><div id="comment-26261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26263"></span>

<div id="answer-container-26263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26263-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can confirm that behavior. Support for <code>3GPP-User-Location-Info</code> has been added in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7474">Bug 7474</a>. Please add a comment with your enhancement request to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7474">Bug 7474</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 16:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26263" class="comments-container"><span id="26268"></span><div id="comment-26268" class="comment"><div id="post-26268-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt,</p><p>we are running a later version 1.10.2 and the 3GPP-User-Location-Info field is not displaying at all in tshark</p></div><div id="comment-26268-info" class="comment-info"><span class="comment-age">(21 Oct '13, 18:23)</span> Nik_NSW_2150</div></div><span id="26271"></span><div id="comment-26271" class="comment"><div id="post-26271-score" class="comment-score"></div><div class="comment-text"><p><strong>Works with 0.99.7 Windows version and TShark 0.99.7 Somewhere between the version 1.10.2 and 0.99.7 there is a bug.</strong></p></div><div id="comment-26271-info" class="comment-info"><span class="comment-age">(21 Oct '13, 20:58)</span> Nik_NSW_2150</div></div><span id="26277"></span><div id="comment-26277" class="comment"><div id="post-26277-score" class="comment-score"></div><div class="comment-text"><p>Please update Bug 7474.</p></div><div id="comment-26277-info" class="comment-info"><span class="comment-age">(22 Oct '13, 00:26)</span> Kurt Knochner ♦</div></div><span id="26298"></span><div id="comment-26298" class="comment"><div id="post-26298-score" class="comment-score"></div><div class="comment-text"><p>Maybe I was not clear . What I am trying to say is that below works for</p><p>TShark 0.99.7 but not for 1.10.2 version</p><p>% tshark -T fields -e radius.Calling_Station_Id -e radius.3GPP_User_Location_Info -E header=y -E separator=, -E quote=d -r TEST_cap.pcap | head radius.Calling_Station_Id,radius.3GPP_User_Location_Info "61498913","01:05:f5:10:55:50:16:5a" "6145563","01:05:f5:10:13:50:2e:4d" "614193","01:05:f5:10:10:50:00:eb"</p></div><div id="comment-26298-info" class="comment-info"><span class="comment-age">(22 Oct '13, 15:42)</span> Nik_NSW_2150</div></div></div><div id="comment-tools-26263" class="comment-tools"></div><div class="clear"></div><div id="comment-26263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

