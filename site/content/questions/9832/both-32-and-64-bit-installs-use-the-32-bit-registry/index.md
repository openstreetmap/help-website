+++
type = "question"
title = "both 32 and 64 bit installs use the 32 bit registry"
description = '''I&#x27;ve noticed that both 32 and 64 bit installs use the 32 bit registry which makes it impossible to distinguish them in the registry. Any workaround on it please?'''
date = "2012-03-29T02:03:00Z"
lastmod = "2012-03-29T13:14:00Z"
weight = 9832
keywords = [ "registry" ]
aliases = [ "/questions/9832" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [both 32 and 64 bit installs use the 32 bit registry](/questions/9832/both-32-and-64-bit-installs-use-the-32-bit-registry)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9832-score" class="post-score" title="current number of votes">0</div><span id="post-9832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've noticed that both 32 and 64 bit installs use the 32 bit registry which makes it impossible to distinguish them in the registry. Any workaround on it please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-registry" rel="tag" title="see questions tagged &#39;registry&#39;">registry</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '12, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/b03373ee92810e5ea4a93fbbcdb72240?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eugenia&#39;s gravatar image" /><p><span>Eugenia</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eugenia has no accepted answers">0%</span></p></div></div><div id="comments-container-9832" class="comments-container"></div><div id="comment-tools-9832" class="comment-tools"></div><div class="clear"></div><div id="comment-9832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9848"></span>

<div id="answer-container-9848" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9848-score" class="post-score" title="current number of votes">2</div><span id="post-9848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure it would make sense for us to explicitly write to the 64-bit view of the registry, at least for our current set of keys. They are either used by the system (e.g. file associations) or by the uninstaller, which is a 32-bit application created by the NSIS installer utility.</p><p>The most reliable way to to find the executable type would probably be to read the value of <code>HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\wireshark.exe</code> then inspect the actual executable, e.g. using <code>file</code> or <code>dumpbin /headers</code>.</p><p>If you want a method based purely on the contents of the registry you could look for "(x86)" in the file path. By default Wireshark is installed in <code>C:\\Program Files\\Wireshark</code> if the executable and system type match and <code>C:\\Program Files (x86)</code> if you're installing the 32-bit version of Wireshark on 64-bit Windows. Note that this isn't 100% reliable since the user can change the installation directory.</p><h3 id="update">Update</h3><p>Starting with the 1.7.1 <code>HKLM\\…\\Uninstall\\Wireshark\\DisplayName</code> and <code>…\\Comments</code> will include a the system type, e.g. "Wireshark 1.7.1 (64-bit)".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '12, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Apr '12, 17:41</strong> </span></p></div></div><div id="comments-container-9848" class="comments-container"></div><div id="comment-tools-9848" class="comment-tools"></div><div class="clear"></div><div id="comment-9848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

