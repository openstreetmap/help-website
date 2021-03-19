+++
type = "question"
title = "Lost Captured Files"
description = '''I recently used Wriehsrak to look through cookies on my computer . I had already chosen which interface I wanted , but later in the capturing decided I wanted to inclued another interface . I was prompted to save my captured packets , I declined . I continued on to select multipule interface , and n...'''
date = "2012-07-17T14:28:00Z"
lastmod = "2012-07-17T15:19:00Z"
weight = 12812
keywords = [ "capture", "packets", "lost" ]
aliases = [ "/questions/12812" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lost Captured Files](/questions/12812/lost-captured-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12812-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently used Wriehsrak to look through cookies on my computer . I had already chosen which interface I wanted , but later in the capturing decided I wanted to inclued another interface . I was prompted to save my captured packets , I declined . I continued on to select multipule interface , and noticed that I had lost a lot of what I had . Is there ANY to retrieve the files that I previously captured , or are they gone for good ? Some , please assist me as soon as possible .</p></div><div id="question-tags" class="tags-container tags">capture packets lost</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '12, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/aa14fbf67f419594de2db066b45fd4cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foxwileykit&#39;s gravatar image" /><p>foxwileykit<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foxwileykit has no accepted answers">0%</span></p></div></div><div id="comments-container-12812" class="comments-container"></div><div id="comment-tools-12812" class="comment-tools"></div><div class="clear"></div><div id="comment-12812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12814"></span>

<div id="answer-container-12814" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12814-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When capturing frames, Wireshark writes them to a temprary file on disk in your temp directory, so if you're lucky you can find them there. The file name usually starts with "wireshark_" and may or may not have an extension.</p><p>Unfortunately Wireshark deletes those temporary capture files when you close it, but it is a good recovery technique for cases where Wireshark crashes while capturing, because then you'll still find the files there.</p><p>Keep in mind: stoping a capture means to kind of "seal" the file. You cannot restart a capture and write into the same file, which is why Wireshark asks you to save it if you do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12814" class="comments-container"><span id="12816"></span><div id="comment-12816" class="comment"><div id="post-12816-score" class="comment-score"></div><div class="comment-text"><p>Jasper actually a good idea. I did not think about that! I tried to recover the temp file with <a href="http://www.piriform.com/recuva">Revuva</a> (it was already installed on the system) right after I restarted capturing and then closed Wireshark. Recuva found some of the temp file names, however the files itself were 'unrecoverable', meaning the tools was unable to identidy the blocks on the disk belonging to the deleted files.</p><p>Anyway, just try it foxwileykit.</p><p>HOWEVER: Don't install anything on that machine, (and don't download anything) as that will write data to disk and possibly overwrite blocks of your deleted temp files. Look for a tool you can run from a USB flash drive. Download it from another machine and then give it a try. Good luck!</p></div><div id="comment-12816-info" class="comment-info"><span class="comment-age">(17 Jul '12, 15:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12814" class="comment-tools"></div><div class="clear"></div><div id="comment-12814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12813"></span>

<div id="answer-container-12813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12813-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>I was prompted to save my captured packets , I declined</code><br />
</p></blockquote><p>I'm sorry, but your captured data is lost, as wireshark kept it only in memory (according to your description). As you declined saving, the allocated memory was "released" and overwritten with new data. There is no way to recover that data.</p><p>If you want to save captured packets in future sessions, I recommend to capture directly to a file.</p><blockquote><p><code>Capture -&gt; Options -&gt; Capture File(s)</code><br />
</p></blockquote><p><strong>UPDATE</strong>: Actually, Wireshark writes a temp file while capturing (<code>%TEMP%\wireshark_n_interfaces_date_time_something</code>, like <code>...\temp\wireshark_2_interfaces_20120718083858_a04512</code>). See answer of @Jasper. That file contains the captured packets. If you restart capturing and decline to save the changes ("Continue without Saving" in the GUI), that temp file will be deleted and a new file will be created, Wireshark start to write data to the new file. Having said that, you can try to recover the deleted temp file with any Undelete software (Windows), however the chances to succeed are pretty bad, as the new temp file might have already overwritten a few (maybe a lot) of the disk blocks of the old file. I did several tests and I was not able to recover any of the temp files. Anyway, I suggest you give it a try!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '12, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '12, 23:51</p></div></div><div id="comments-container-12813" class="comments-container"><span id="12817"></span><div id="comment-12817" class="comment"><div id="post-12817-score" class="comment-score"></div><div class="comment-text"><p>Actually, Jasper's correct here - Wireshark saves captured packets in a temporary file, rather than storing them only in its address space. "Capture directly to a file" really means "capture directly to a <em>non-temporary</em> file".</p><p>However, the key here is "temporary" - Wireshark deletes the temporary file if you quit without saving it. The only time the temporary file will still be around is if Wireshark were to crash and thus not have the opportunity to remove the temporary file. Otherwise, you'd have to hope that there's some way to recover a deleted file.</p></div><div id="comment-12817-info" class="comment-info"><span class="comment-age">(17 Jul '12, 20:14)</span> Guy Harris ♦♦</div></div><span id="12818"></span><div id="comment-12818" class="comment"><div id="post-12818-score" class="comment-score"></div><div class="comment-text"><p>yep. See my comment in Jaspers answer ;-)</p></div><div id="comment-12818-info" class="comment-info"><span class="comment-age">(17 Jul '12, 22:30)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12813" class="comment-tools"></div><div class="clear"></div><div id="comment-12813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

