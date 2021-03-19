+++
type = "question"
title = "No Disk error displayed by Wireshark"
description = '''Is there a setting to prevent Wireshark to check the CD/DVD drive when launching? If I do not use my DVD drive, Wireshark launches with no errors. However, if I use my DVD drive and try to launch Wireshark, I receive the following error: &quot;There is no disk in the drive. Please insert a disk into driv...'''
date = "2015-03-24T09:04:00Z"
lastmod = "2015-04-02T09:07:00Z"
weight = 40806
keywords = [ "disk", "error", "no" ]
aliases = [ "/questions/40806" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No Disk error displayed by Wireshark](/questions/40806/no-disk-error-displayed-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40806-score" class="post-score" title="current number of votes">0</div><span id="post-40806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a setting to prevent Wireshark to check the CD/DVD drive when launching? If I do not use my DVD drive, Wireshark launches with no errors. However, if I use my DVD drive and try to launch Wireshark, I receive the following error: "There is no disk in the drive. Please insert a disk into drive D:" This error is displayed even when not accessing a Wireshark file on the DVD. For example, the DVD has JPEG files. I open some files on the DVD. I then remove the DVD and launch Wireshark. The "No Disk" error is then displayed.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disk" rel="tag" title="see questions tagged &#39;disk&#39;">disk</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '15, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-40806" class="comments-container"></div><div id="comment-tools-40806" class="comment-tools"></div><div class="clear"></div><div id="comment-40806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40808"></span>

<div id="answer-container-40808" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40808-score" class="post-score" title="current number of votes">0</div><span id="post-40808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you've got a trace file link to your DVD drive in your recent files list? Can you clear those in "File -&gt; Recent Files -&gt; Clear" and try again?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40808" class="comments-container"><span id="40810"></span><div id="comment-40810" class="comment"><div id="post-40810-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper - I just tested it and the error still occurs. My procedure used for testing: 1. Launch Wireshark and go to "File -&gt; Open Recent -&gt; Clear recent files" 2. Quit Wireshark 3. Load a DVD and open a text file 4. Launch Wireshark. Error is displayed. The only way to get rid of the error from displaying whenever launching Wireshark is to reboot the computer.</p></div><div id="comment-40810-info" class="comment-info"><span class="comment-age">(24 Mar '15, 09:47)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="40837"></span><div id="comment-40837" class="comment"><div id="post-40837-score" class="comment-score"></div><div class="comment-text"><p>In your question your removed the DVD before launching Wireshark, in this comment you have still a text file open on the DVD. Difference in use case?</p></div><div id="comment-40837-info" class="comment-info"><span class="comment-age">(25 Mar '15, 07:29)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="40839"></span><div id="comment-40839" class="comment"><div id="post-40839-score" class="comment-score"></div><div class="comment-text"><p>Sorry - I forgot a few steps. 3(a). Close text file that was launched from DVD directory. 3(b). Remove DVD from PC. After removing the DVD, there are no other DVD's placed within the drive. When launching Wireshark, I receive the error: "There is no disk in the drive. Please insert a disk into drive D:" - where drive D: is my DVD drive. This error is seen even after clearing the recent files within Wireshark: File-&gt;Open Recent-&gt;Clear recent files</p></div><div id="comment-40839-info" class="comment-info"><span class="comment-age">(25 Mar '15, 07:45)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="40877"></span><div id="comment-40877" class="comment"><div id="post-40877-score" class="comment-score"></div><div class="comment-text"><p>One other thing I can think of is the File Open dialog. Wireshark remembers what the last path was which was used to open a file. Does that still point to the DVD? The value is also stored in your 'recent' file under the key gui.fileopen_remembered_dir.</p></div><div id="comment-40877-info" class="comment-info"><span class="comment-age">(26 Mar '15, 02:39)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="41151"></span><div id="comment-41151" class="comment"><div id="post-41151-score" class="comment-score"></div><div class="comment-text"><p>Both values (File Open dialog and gui.fileopen_remembered_dir) are both set to my hard-drive (C:/) before and after inserting a DVD in the DVD drive. Also, after removing the DVD in the DVD drive, these values are still set to the hard drive (C:/). I am beginning to think it is a Windows issue?</p></div><div id="comment-41151-info" class="comment-info"><span class="comment-age">(02 Apr '15, 09:07)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-40808" class="comment-tools"></div><div class="clear"></div><div id="comment-40808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

