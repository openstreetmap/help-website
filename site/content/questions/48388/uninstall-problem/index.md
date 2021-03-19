+++
type = "question"
title = "Uninstall problem"
description = '''I download Wireshark 2.0.0 32bit release. And install in my programms folder (D:/Programms/). I reboot my system and uninstall Wireshark (this version does not work on my WinXP). And after that all other files in /Programs derictory was disappeared. Its look like Wireshark uninstall deleted hims.'''
date = "2015-12-09T12:37:00Z"
lastmod = "2015-12-10T09:25:00Z"
weight = 48388
keywords = [ "problem", "uninstall" ]
aliases = [ "/questions/48388" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Uninstall problem](/questions/48388/uninstall-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48388-score" class="post-score" title="current number of votes">0</div><span id="post-48388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I download Wireshark 2.0.0 32bit release. And install in my programms folder (D:/Programms/). I reboot my system and uninstall Wireshark (this version does not work on my WinXP). And after that all other files in /Programs derictory was disappeared. Its look like Wireshark uninstall deleted hims.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '15, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/e12caeb22c534a56980be122f2484b98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nielo&#39;s gravatar image" /><p><span>Nielo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nielo has no accepted answers">0%</span></p></div></div><div id="comments-container-48388" class="comments-container"><span id="48391"></span><div id="comment-48391" class="comment"><div id="post-48391-score" class="comment-score"></div><div class="comment-text"><p>I repeat install-uninstallation. And this happened again. Be careful.</p></div><div id="comment-48391-info" class="comment-info"><span class="comment-age">(09 Dec '15, 13:16)</span> <span class="comment-user userinfo">Nielo</span></div></div><span id="48393"></span><div id="comment-48393" class="comment"><div id="post-48393-score" class="comment-score"></div><div class="comment-text"><p>Very odd.</p><p>I tried to replicate it here, using Win 8.1 x64, I created a directory D:\Programs, and installed Wireshark to D:\Programs\Wireshark. The uninstall removed the Wireshark subdirectory but left D:\Programs intact along with some other entries I'd made in there.</p><p>I then repeated the install, this time into D:\Programs, this installed Wireshark directly into the specified directory. Uninstalling then tried to delete the directory but was unable to and displayed an error message to indicate this, but apart from that all traces of Wireshark were removed, and the D:\Programs directory was left as before.</p><p>What did you enter into the installer directory field? It should be the name of a directory specifically for Wireshark. Presuming you use D:\Progams for multiple applications, you should enter D:\Programs\Wireshark.</p></div><div id="comment-48393-info" class="comment-info"><span class="comment-age">(09 Dec '15, 14:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48400"></span><div id="comment-48400" class="comment"><div id="post-48400-score" class="comment-score"></div><div class="comment-text"><p>Thanks for answer.</p><p>Yes, if select "D:\Programs" in itstall setup file browser, automatically creates \Wireshark, so I install it in D:\Programs\Wireshark.</p><p>But I think the problem is not here. In first and second time I install all components, including USBPcap. When the USBPcap installation is to start up, I also select D:\Programs. And when I launched Wireshark uninstallation and choose delete all components (including USBPcap), all other files in \Programs were removed. Here is my mistake, it was necessary to manually create a subfolder for USBPcap. But why USBPcap uninstallation setup deleted other files in \Programs? Should not it only delete USBPcap-files?</p></div><div id="comment-48400-info" class="comment-info"><span class="comment-age">(09 Dec '15, 15:22)</span> <span class="comment-user userinfo">Nielo</span></div></div><span id="48401"></span><div id="comment-48401" class="comment"><div id="post-48401-score" class="comment-score"></div><div class="comment-text"><p>I already had USBPCap installed so didn't install or remove it in my tests.</p><p>I'll have to try that.</p></div><div id="comment-48401-info" class="comment-info"><span class="comment-age">(09 Dec '15, 15:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48388" class="comment-tools"></div><div class="clear"></div><div id="comment-48388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48417"></span>

<div id="answer-container-48417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48417-score" class="post-score" title="current number of votes">0</div><span id="post-48417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is indeed an issue with USBPcap installer that assumes USBPcap will be installed in a dedicated folder. I modified it locally and we will try to ship a modified version of the installer in the next Wireshark release. Thanks for reporting the issue.</p><p>Edit: the patch set can be found here <a href="https://code.wireshark.org/review/#/c/12546/">https://code.wireshark.org/review/#/c/12546/</a> and will be integrated for Wireshark 2.0.1</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '15, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Dec '15, 14:52</strong> </span></p></div></div><div id="comments-container-48417" class="comments-container"><span id="48424"></span><div id="comment-48424" class="comment"><div id="post-48424-score" class="comment-score"></div><div class="comment-text"><p>Wireshark also assumes a dedicated directory, but the uninstaller, on my machine at least, was unable to delete the common directory I installed it in.</p><p>Not sure if we can guard against that somehow.</p></div><div id="comment-48424-info" class="comment-info"><span class="comment-age">(10 Dec '15, 08:02)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48425"></span><div id="comment-48425" class="comment"><div id="post-48425-score" class="comment-score"></div><div class="comment-text"><p>We can at least modify the uninstaller script so that it does not erase the installation folder if not empty - what USBPcap installer was doing. :)</p></div><div id="comment-48425-info" class="comment-info"><span class="comment-age">(10 Dec '15, 09:01)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="48427"></span><div id="comment-48427" class="comment"><div id="post-48427-score" class="comment-score"></div><div class="comment-text"><p>I think that must be the case already then for Wireshark as I got an error message when it tried (or checked).</p></div><div id="comment-48427-info" class="comment-info"><span class="comment-age">(10 Dec '15, 09:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48428"></span><div id="comment-48428" class="comment"><div id="post-48428-score" class="comment-score"></div><div class="comment-text"><p>yes, we are not adding the evil /R flag to RMDir "$INSTDIR" :)</p></div><div id="comment-48428-info" class="comment-info"><span class="comment-age">(10 Dec '15, 09:25)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-48417" class="comment-tools"></div><div class="clear"></div><div id="comment-48417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

