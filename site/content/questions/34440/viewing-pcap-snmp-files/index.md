+++
type = "question"
title = "Viewing PCAP SNMP Files"
description = '''Hi I have PCAP files that contain SNMP traps from Oracle. I have the MIB&#x27;s and I have added the MIB&#x27;s to the mibs directory c:/programs/wireshark/snmp/mibs. I have added the mibs to the list of modules under name resolution.  But Wireshark still doesnt resolve the varbinds in the trap. I tried to ad...'''
date = "2014-07-06T08:53:00Z"
lastmod = "2014-07-08T11:32:00Z"
weight = 34440
keywords = [ "pcap", "mib", "snmp", "trap" ]
aliases = [ "/questions/34440" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Viewing PCAP SNMP Files](/questions/34440/viewing-pcap-snmp-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34440-score" class="post-score" title="current number of votes">0</div><span id="post-34440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have PCAP files that contain SNMP traps from Oracle.</p><p>I have the MIB's and I have added the MIB's to the mibs directory c:/programs/wireshark/snmp/mibs. I have added the mibs to the list of modules under name resolution.</p><p>But Wireshark still doesnt resolve the varbinds in the trap.</p><p>I tried to add a new path to that directory (wouldnt have thought I would need to since its wiresharks default directory) but wireshark doesnt allow me to do that.</p><p>I have created a new directory but that didnt work either.</p><p>Getting really desperate. Can you please help and provide details guide to installing mibs?</p><p>cheers ............. Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-mib" rel="tag" title="see questions tagged &#39;mib&#39;">mib</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span> <span class="post-tag tag-link-trap" rel="tag" title="see questions tagged &#39;trap&#39;">trap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/e4977723086cc581cbb74c30bc5f38a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulSNZ&#39;s gravatar image" /><p><span>PaulSNZ</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulSNZ has no accepted answers">0%</span></p></div></div><div id="comments-container-34440" class="comments-container"><span id="34441"></span><div id="comment-34441" class="comment"><div id="post-34441-score" class="comment-score"></div><div class="comment-text"><p>What version of wireshark are you using? Wireshark uses libsmi to parse miss. Libsmi can be really picky about the format of the mibs. Try running them trough the libsmi mib checker.</p></div><div id="comment-34441-info" class="comment-info"><span class="comment-age">(06 Jul '14, 13:01)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="34469"></span><div id="comment-34469" class="comment"><div id="post-34469-score" class="comment-score"></div><div class="comment-text"><p>is it possible to post a small sample capture file and the required MIB files on google drive or dropbox?</p></div><div id="comment-34469-info" class="comment-info"><span class="comment-age">(08 Jul '14, 09:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="34472"></span><div id="comment-34472" class="comment"><div id="post-34472-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>I dont have either set up however if you send me a mail to <span class="__cf_email__" data-cfemail="cabaabbfa6e4b9e4a4b08aada7aba3a6e4a9a5a7">[email protected]</span> I can reply with the files and mibs.</p><p>cheers ........... Paul</p></div><div id="comment-34472-info" class="comment-info"><span class="comment-age">(08 Jul '14, 09:46)</span> <span class="comment-user userinfo">PaulSNZ</span></div></div><span id="34475"></span><div id="comment-34475" class="comment"><div id="post-34475-score" class="comment-score"></div><div class="comment-text"><p>Paul,</p><p>I would prefer if you could post the files somewhere (google drive, dropbox, etc.) and then post the link here, so everybody here gets a chance to look at the files.</p><p>If you don't want that, please take a look at my profile (click on my name) to get my e-mail address.</p><p>Regards<br />
Kurt</p></div><div id="comment-34475-info" class="comment-info"><span class="comment-age">(08 Jul '14, 11:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34440" class="comment-tools"></div><div class="clear"></div><div id="comment-34440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

