+++
type = "question"
title = "Decode as not showing protocol"
description = '''Hello, I&#x27;m running Wireshark 2.01 to decode CIP Motion packets. I had this setup working this morning, then suddenly it stopped decoding the UDP port 2222 as CIP Motion. I restarted Wireshark and the computer to no avail. I went back into Decode As and the field I had created disappeared. I went to ...'''
date = "2016-02-02T10:43:00Z"
lastmod = "2016-02-02T10:43:00Z"
weight = 49732
keywords = [ "motion" ]
aliases = [ "/questions/49732" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode as not showing protocol](/questions/49732/decode-as-not-showing-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49732-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm running Wireshark 2.01 to decode CIP Motion packets. I had this setup working this morning, then suddenly it stopped decoding the UDP port 2222 as CIP Motion. I restarted Wireshark and the computer to no avail. I went back into Decode As and the field I had created disappeared. I went to re-create it, and CIP Motion is not available. I checked the installed and enabled dissectors, and CIP Motion is there and enabled.</p><p>Any ideas? I'm about to uninstall and go back to 1.12 and hopefully that works.</p><p>Thanks, Jim</p></div><div id="question-tags" class="tags-container tags">motion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/1a6e3fa77f556903b17e3480b2adcdb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsmart&#39;s gravatar image" /><p>jsmart<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsmart has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Feb '16, 05:23</p></div></div><div id="comments-container-49732" class="comments-container"><span id="49771"></span><div id="comment-49771" class="comment"><div id="post-49771-score" class="comment-score"></div><div class="comment-text"><p>Can you publish the capture (or a few packets of it) and the <code>preferences</code> file from your profile somewhere and put a link to them here?</p></div><div id="comment-49771-info" class="comment-info"><span class="comment-age">(03 Feb '16, 06:40)</span> sindy</div></div><span id="49773"></span><div id="comment-49773" class="comment"><div id="post-49773-score" class="comment-score"></div><div class="comment-text"><p>I think it's probably not Wireshark. I had switched from using a managed switch to a basic hub in trying to see if the switch was blocking some packets. However, when on the hub, it seems Wireshark now sometimes decodes properly and sometimes doesn't.</p></div><div id="comment-49773-info" class="comment-info"><span class="comment-age">(03 Feb '16, 07:01)</span> jsmart</div></div><span id="49778"></span><div id="comment-49778" class="comment"><div id="post-49778-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I think it's probably not Wireshark.</p></blockquote><p>well, it's probably not Wireshark's <em>configuration</em>, but it may still be something about the contents of some of the packets, which prevents Wireshark from decoding valid packets correctly, as well as really invalid (malformed, blocked) packets. The more the captures from both sources (switch and hub) would be interesting to analyse.</p></div><div id="comment-49778-info" class="comment-info"><span class="comment-age">(03 Feb '16, 07:41)</span> sindy</div></div></div><div id="comment-tools-49732" class="comment-tools"></div><div class="clear"></div><div id="comment-49732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

