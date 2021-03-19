+++
type = "question"
title = "Wireshark 1.6.0 frequently crashes XP-32bit"
description = '''I am opening/closing several capture files (originally captured in 1.6.0 too) using 1.6.0. I am just looking at summary statistics. It seems to be a frequent event for Wireshark to close with an error in libwireshark.dll v1.6.0.37592. This is getting rather frustrating to have to keep opening back u...'''
date = "2011-06-13T13:54:00Z"
lastmod = "2011-06-13T13:54:00Z"
weight = 4546
keywords = [ "windows", "crash" ]
aliases = [ "/questions/4546" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.6.0 frequently crashes XP-32bit](/questions/4546/wireshark-160-frequently-crashes-xp-32bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4546-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am opening/closing several capture files (originally captured in 1.6.0 too) using 1.6.0. I am just looking at summary statistics. It seems to be a frequent event for Wireshark to close with an error in libwireshark.dll v1.6.0.37592. This is getting rather frustrating to have to keep opening back up Wireshark.</p><p>The capture files are on the local C: drive. They range anywhere from 197K to 35M so they are not large nor are they complex protocol decodes - simple SharePoint &amp; SMB traffic.</p><p>Any suggestions on fixes?</p></div><div id="question-tags" class="tags-container tags">windows crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '11, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/d1f7fabf169915dc5ba93025794b84db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Labnuke&#39;s gravatar image" /><p>Labnuke<br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Labnuke has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 13 Jun '11, 15:41</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4546" class="comments-container"><span id="4549"></span><div id="comment-4549" class="comment"><div id="post-4549-score" class="comment-score"></div><div class="comment-text"><p>What exactly is the error message? Can you share the pcap (strip any proprietary data) via <a href="http://min.us">min.us</a>? If not, I can try reproducing the behavior if you describe the steps in detail.</p></div><div id="comment-4549-info" class="comment-info"><span class="comment-age">(13 Jun '11, 15:38)</span> helloworld</div></div><span id="4562"></span><div id="comment-4562" class="comment"><div id="post-4562-score" class="comment-score"></div><div class="comment-text"><p>It happens on various capture files and is not repeatable on the same cap file. The error logged in the system application event log is: Faulting application wireshark.exe, version 1.6.0.37592, faulting module libwireshark.dll, version 1.6.0.3792, fault address (this address varies).</p><p>I am simply clicking the Open file folder icon on the toolbar and just picking a different cap file in a folder with about 70 different capture files. As shown above, the file sizes are not large and file content is not complex.</p></div><div id="comment-4562-info" class="comment-info"><span class="comment-age">(14 Jun '11, 04:28)</span> Labnuke</div></div></div><div id="comment-tools-4546" class="comment-tools"></div><div class="clear"></div><div id="comment-4546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

