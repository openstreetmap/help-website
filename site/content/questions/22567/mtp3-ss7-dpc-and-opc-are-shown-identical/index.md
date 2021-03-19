+++
type = "question"
title = "MTP3 - SS7 DPC and OPC are shown identical"
description = '''Hello: When I decode a MTP3 section (SS7 with CAMEL-v2 protocol), Wireshark indicate that the SOURCE and DESTINATION Point Code are the same (always is the OPC for both values). Actually, when you see the decodification part below, you look OK (i.e. OPC and DPC are different). I observed this error ...'''
date = "2013-07-02T11:46:00Z"
lastmod = "2013-07-03T15:57:00Z"
weight = 22567
keywords = [ "dpc", "ss7", "opc", "mtp3", "camel" ]
aliases = [ "/questions/22567" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [MTP3 - SS7 DPC and OPC are shown identical](/questions/22567/mtp3-ss7-dpc-and-opc-are-shown-identical)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22567-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello:<br />
When I decode a MTP3 section (SS7 with CAMEL-v2 protocol), Wireshark indicate that the SOURCE and DESTINATION Point Code are the same (always is the OPC for both values).<br />
Actually, when you see the decodification part below, you look OK (i.e. OPC and DPC are different).</p><p>I observed this error -at least - in this versions: Wireshark-win32-1.8.4, Wireshark-win32-1.8.6 and Wireshark-win32-1.10.0 (last stable version available).</p><p>OS: WinXP (5.1.2600)/32 bit.</p><p>Regards. Miguel Quintana.</p></div><div id="question-tags" class="tags-container tags">dpc ss7 opc mtp3 camel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/ddd785174dc48e3284828f386b2082c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mquintanap&#39;s gravatar image" /><p>mquintanap<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mquintanap has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-22567" class="comments-container"><span id="22575"></span><div id="comment-22575" class="comment"><div id="post-22575-score" class="comment-score"></div><div class="comment-text"><p>can you please add a sample capture file (google docs, dropbox) or a screenshot?</p></div><div id="comment-22575-info" class="comment-info"><span class="comment-age">(02 Jul '13, 14:12)</span> Kurt Knochner ♦</div></div><span id="22579"></span><div id="comment-22579" class="comment"><div id="post-22579-score" class="comment-score"></div><div class="comment-text"><p>What MTP3 format are you using (ANSI, ITU, China)? I understand that Wireshark 1.10 has added a heuristic check to decide what point code format to use for MTP3, but you should still be able to manually go to Preferences &gt; Protocols &gt; MTP3 and specify it.</p><p>I'm confused by the question though. You say that Wireshark is decoding both OPC and DPC as being the same point code number? Are you putting these in decimal, dot-decimal or is it the same regardless of protocol settings? A picture file would be helpful, as well as the trace and your current MTP3 protocol preference configuration.</p><p>You mention Camel phase 2 here. Is there a problem decoding that application at all? How is Camel relevant if we're talking about OPC and DPC values? If there's an issue with the decoding of Camel layer, I believe that dissector is called based on the SSN so if you're using a non-default SSN you may want to check the Preferences &gt; Protocols &gt; Camel section of Wireshark and make sure that the SSN you're using for Camel queries is listed there, otherwise it won't decode properly.</p><p>edit: updated to a comment since it's more questions than answers. :)</p></div><div id="comment-22579-info" class="comment-info"><span class="comment-age">(02 Jul '13, 15:19)</span> Quadratic</div></div><span id="22622"></span><div id="comment-22622" class="comment"><div id="post-22622-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>Below are the screenshot and the MTP3 preferences. We're using ITU format. In this case, I'm working with a CAMEL v2 trace, this is not relevant like you said (just for tell you the nature of the trace) and there's not problem decoding that part. With an ISUP capture appears the same behaviour. In fact ISUP, CAMEL and others protocols that i'm working are only transported by MTP3.</p><p>I thought it could be our MTP2 application who was logging corrupted files; but when I process the same captures (Camel and ISUP) with a Linux Version no problem arises. I will upload some traces soon.</p><p>Regards, Miguel.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wspserror.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/mtp3_preferences.JPG" alt="alt text" /></p></div><div id="comment-22622-info" class="comment-info"><span class="comment-age">(03 Jul '13, 15:04)</span> mquintanap</div></div><span id="22625"></span><div id="comment-22625" class="comment"><div id="post-22625-score" class="comment-score"></div><div class="comment-text"><p>Thanks. If you can post a sample capture with that problem I can compare it with my 1.10 install on Windows. I work with MTP traces every day in 1.8 and 1.10 without seeing this issue, though not often in ITU format and usually in the context of M3UA.</p></div><div id="comment-22625-info" class="comment-info"><span class="comment-age">(03 Jul '13, 16:27)</span> Quadratic</div></div></div><div id="comment-tools-22567" class="comment-tools"></div><div class="clear"></div><div id="comment-22567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22624"></span>

<div id="answer-container-22624" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22624-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see that effect with a sample capture file on Windows with Wireshark 1.10.0</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=camel2.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=camel2.pcap</a></p></blockquote><p>As you say the problem does not show up on Linux, maybe the definition of your columns has somehow changed on Windows.</p><p>To check, please right click on the <strong>Source</strong> and <strong>Destination</strong> column and then select "Edit Column Details". You should see "Source address" and "Destination address" in the 'Field type'. If that is <strong>not</strong> the case, please change it to the expected values.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '13, 15:59</p></div></div><div id="comments-container-22624" class="comments-container"><span id="22667"></span><div id="comment-22667" class="comment"><div id="post-22667-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt, Finally that was the problem. For some reason the "Field Type" it was changed. I didn't know that the "Title" it's only a name reference and you can change the "Field Type" and put there any value...</p><p>Thanks everyone for your help.</p><p>Regards, Miguel Quintana.</p></div><div id="comment-22667-info" class="comment-info"><span class="comment-age">(04 Jul '13, 11:17)</span> mquintanap</div></div></div><div id="comment-tools-22624" class="comment-tools"></div><div class="clear"></div><div id="comment-22624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22623"></span>

<div id="answer-container-22623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22623-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm a little suspicious of the MTP3 dissector code, as it's using global variables - <code>mtp3_addr_dpc</code> and <code>mtp3_addr_opc</code> - in ways that <em>might</em> cause issues.</p><p>Please file a bug on this at <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>, so that we can track this. (Give the symptoms, not my theory, as the problem; just cite my theory as one possibility.) Upload captures by attaching them to the bug rather than uploading them to Cloudshark or a site such as that. Also re-attach the screenshot to the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '13, 15:29</p></div></div><div id="comments-container-22623" class="comments-container"></div><div id="comment-tools-22623" class="comment-tools"></div><div class="clear"></div><div id="comment-22623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

