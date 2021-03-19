+++
type = "question"
title = "Wireshark gets stuck at 99% loaded on Windows 7 64-bit"
description = '''Newest build just downloaded to try and fix start-up problem I am getting. Gets to 99% and freezes. So this is with the last 2 versions. Any ideas? Win 7 Pro 64bit NB I thought I had already asked this but it shows up blank, so if there ends up a repeat, I am sorry. Fixed but don&#x27;t know why.  I did ...'''
date = "2015-10-19T20:18:00Z"
lastmod = "2015-10-26T01:45:00Z"
weight = 46741
keywords = [ "99", "load", "percent", "win7", "freezes" ]
aliases = [ "/questions/46741" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark gets stuck at 99% loaded on Windows 7 64-bit](/questions/46741/wireshark-gets-stuck-at-99-loaded-on-windows-7-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46741-score" class="post-score" title="current number of votes">0</div><span id="post-46741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Newest build just downloaded to try and fix start-up problem I am getting. Gets to 99% and freezes. So this is with the last 2 versions. Any ideas? Win 7 Pro 64bit NB I thought I had already asked this but it shows up blank, so if there ends up a repeat, I am sorry. Fixed but don't know why. I did have wireshark off the PC for a week now and reinstalled the very same download and this time started fine. I was going to load a screen shot. It has asked for update to be done within a minute of starting and it ran OK. Go figure. Got me puzzled. Thanks for the suggestions guys ( n gals if there are any)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-99" rel="tag" title="see questions tagged &#39;99&#39;">99</span> <span class="post-tag tag-link-load" rel="tag" title="see questions tagged &#39;load&#39;">load</span> <span class="post-tag tag-link-percent" rel="tag" title="see questions tagged &#39;percent&#39;">percent</span> <span class="post-tag tag-link-win7" rel="tag" title="see questions tagged &#39;win7&#39;">win7</span> <span class="post-tag tag-link-freezes" rel="tag" title="see questions tagged &#39;freezes&#39;">freezes</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/7cb7cac39f35a771fcc09733b4d077b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quiet%20Probee&#39;s gravatar image" /><p><span>Quiet Probee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quiet Probee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '15, 15:06</strong> </span></p></div></div><div id="comments-container-46741" class="comments-container"><span id="46749"></span><div id="comment-46749" class="comment"><div id="post-46749-score" class="comment-score"></div><div class="comment-text"><p>As my cristal ball is currently in the cellar, I have to bother you with some questions:</p><ul><li>what is your OS and OS version</li><li>what is your Wireshark version</li><li>please define 'Gets to 99% and freezes'</li><li>can you add screenshots</li></ul></div><div id="comment-46749-info" class="comment-info"><span class="comment-age">(20 Oct '15, 03:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46741" class="comment-tools"></div><div class="clear"></div><div id="comment-46741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46753"></span>

<div id="answer-container-46753" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46753-score" class="post-score" title="current number of votes">0</div><span id="post-46753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Usually this is a sign of WinPcap failing to load properly. Are you running on Windows 8? You could eventually try to reinstall WinPcap. See <a href="https://ask.wireshark.org/questions/26517/winpcap-seems-to-crash-on-win81">https://ask.wireshark.org/questions/26517/winpcap-seems-to-crash-on-win81</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '15, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-46753" class="comments-container"><span id="46919"></span><div id="comment-46919" class="comment"><div id="post-46919-score" class="comment-score"></div><div class="comment-text"><p>Sorry for late reply (National holiday) Im using win 7 pro 64bit and WinPcap4.1.3 . I presumed that WinPcap is the latest bundled with wireshark latest version (just checked now and is) and after complete uninstall - reinstall , I still get wireshark loading to 99% and freezing. Tried starting WinPcap1st and then wireshark but no change, "Loading module Preferences 99% "</p></div><div id="comment-46919-info" class="comment-info"><span class="comment-age">(25 Oct '15, 15:37)</span> <span class="comment-user userinfo">Quiet Probee</span></div></div><span id="46920"></span><div id="comment-46920" class="comment"><div id="post-46920-score" class="comment-score"></div><div class="comment-text"><p>Also under windows 7, there is no &lt;start to="" 0x3=""&gt; when looking for it under HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NPF\Enum as suggested. Is windows different to windows 8 ?</p></div><div id="comment-46920-info" class="comment-info"><span class="comment-age">(25 Oct '15, 15:47)</span> <span class="comment-user userinfo">Quiet Probee</span></div></div></div><div id="comment-tools-46753" class="comment-tools"></div><div class="clear"></div><div id="comment-46753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46923"></span>

<div id="answer-container-46923" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46923-score" class="post-score" title="current number of votes">0</div><span id="post-46923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>and after complete uninstall - reinstall , I still get wireshark loading to 99% and freezing.</p></blockquote><p>The reason could be a somehow broken config file. You'll find the folder being used on your system in the Help menu</p><blockquote><p>Help -&gt; About Wiresahrk -&gt; Folders [TAB]</p></blockquote><p>See "Personal Configuration".</p><p>Save the files (if you need them) and then remove all files. Then start Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46923" class="comments-container"></div><div id="comment-tools-46923" class="comment-tools"></div><div class="clear"></div><div id="comment-46923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

