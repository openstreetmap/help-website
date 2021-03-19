+++
type = "question"
title = "Can&#x27;t download or install WS"
description = '''Hello, I&#x27;m having some trouble downloading WS (tried two versions) on a Vista 64-bit laptop. I&#x27;m getting an error Directory name is invalid. With this laptop, running with 7, I can&#x27;t install and I get the error message error opening file for writing c:&#92;Program Files&#92;Wireshark&#92;wiretap-1.6.0.dll. Any ...'''
date = "2012-01-24T16:21:00Z"
lastmod = "2012-01-24T23:45:00Z"
weight = 8593
keywords = [ "download-install", "ws" ]
aliases = [ "/questions/8593" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't download or install WS](/questions/8593/cant-download-or-install-ws)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8593-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm having some trouble downloading WS (tried two versions) on a Vista 64-bit laptop. I'm getting an error <em>Directory name is invalid</em>. With this laptop, running with 7, I can't install and I get the error message error opening file for writing c:\Program Files\Wireshark\wiretap-1.6.0.dll. Any idea is welcome. Thanks in advance</p></div><div id="question-tags" class="tags-container tags">download-install ws</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '12, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/a2cec2b9ead767b88b86818bb9ee9c7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kakougne&#39;s gravatar image" /><p>kakougne<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kakougne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '12, 23:42</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-8593" class="comments-container"></div><div id="comment-tools-8593" class="comment-tools"></div><div class="clear"></div><div id="comment-8593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8596"></span>

<div id="answer-container-8596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8596-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you got problems with downloading the installer, resulting in a bad/broken setup file. You might want to check if it was downloaded correctly; I just created an MD5 hash of the 64bit setup file "wireshark-win64-1.6.5.exe" (which worked fine on install on my PC) - check if your MD5 hash matches mine: A43C22C98B914FE60812995C000E2411.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '12, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8596" class="comments-container"><span id="8764"></span><div id="comment-8764" class="comment"><div id="post-8764-score" class="comment-score"></div><div class="comment-text"><p>I just had the same error but on Win7 Enterprise 64bit. I ran the hash above and it was fine.</p></div><div id="comment-8764-info" class="comment-info"><span class="comment-age">(01 Feb '12, 22:04)</span> ptrivino</div></div><span id="8766"></span><div id="comment-8766" class="comment"><div id="post-8766-score" class="comment-score"></div><div class="comment-text"><p>Better refer to <a href="http://wiresharkdownloads.riverbed.com/wireshark/SIGNATURES-1.6.5.txt">the official download site signatures file</a>. Your hash is ok by the way :)</p></div><div id="comment-8766-info" class="comment-info"><span class="comment-age">(01 Feb '12, 23:31)</span> Jaap ♦</div></div><span id="8768"></span><div id="comment-8768" class="comment"><div id="post-8768-score" class="comment-score"></div><div class="comment-text"><p>Thx Jaap, I looked for hashes on the download page but was to blind to see the link at the bottom of the page - bad case of not enough coffee in the evening I guess ;-)</p></div><div id="comment-8768-info" class="comment-info"><span class="comment-age">(02 Feb '12, 00:01)</span> Jasper ♦♦</div></div><span id="8769"></span><div id="comment-8769" class="comment"><div id="post-8769-score" class="comment-score"></div><div class="comment-text"><p>@ptrivino: do you have administator rights? Can you run the installer with "run as administrator"? Maybe a virus scanner or other "security tool" is blocking installs?</p></div><div id="comment-8769-info" class="comment-info"><span class="comment-age">(02 Feb '12, 00:03)</span> Jasper ♦♦</div></div><span id="15198"></span><div id="comment-15198" class="comment"><div id="post-15198-score" class="comment-score"></div><div class="comment-text"><p>Wireshark install doesn't prompt for "run as admin" and I missed that during the install (my fault). But The install completes with some errors that I originally thought were with it trying to remove the currently installed version (which was no longer there). I think now it was errors that it couldn't write the new file to the install dir - but wait, the install dir doesn't exist either! You would think the install program would check to see if the install dir got created before dumping files to it (their fault). At the end of the install (which completed successfully) it asked if I wanted to run WS after install. It of course couldn't and didn't.</p></div><div id="comment-15198-info" class="comment-info"><span class="comment-age">(23 Oct '12, 11:22)</span> billjam54</div></div><span id="15202"></span><div id="comment-15202" class="comment not_top_scorer"><div id="post-15202-score" class="comment-score"></div><div class="comment-text"><p>@billjam54</p><p>Do you have UAC disabled? The installer must run as administrator to write into "Program Files".</p></div><div id="comment-15202-info" class="comment-info"><span class="comment-age">(23 Oct '12, 14:38)</span> grahamb ♦</div></div></div><div id="comment-tools-8596" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-8596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

