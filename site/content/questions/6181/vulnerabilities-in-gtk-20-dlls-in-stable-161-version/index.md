+++
type = "question"
title = "Vulnerabilities in GTK+ 2.0 dll&#x27;s in stable 1.6.1 version?"
description = '''see: http://secunia.com/advisories/45815/ the 1.6.1 wireshark stable version contains the vulnerable version is a new wireshark on its way? Or is this not true? see below Description A vulnerability has been reported in GTK+, which can be exploited by malicious people to compromise an application us...'''
date = "2011-09-07T06:44:00Z"
lastmod = "2011-09-07T10:56:00Z"
weight = 6181
keywords = [ "secunia-psi", "vulnerability", "gtk+" ]
aliases = [ "/questions/6181" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Vulnerabilities in GTK+ 2.0 dll's in stable 1.6.1 version?](/questions/6181/vulnerabilities-in-gtk-20-dlls-in-stable-161-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6181-score" class="post-score" title="current number of votes">0</div><span id="post-6181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>see: http://secunia.com/advisories/45815/ the 1.6.1 wireshark stable version contains the vulnerable version is a new wireshark on its way? Or is this not true? see below</p><p>Description</p><p>A vulnerability has been reported in GTK+, which can be exploited by malicious people to compromise an application using the library.</p><p>The vulnerability is caused due to the "_gdk_input_wintab_init_check()" (gdk/win32/gdkinput-win32.c) and the "xp_theme_init()" functions (modules/engines/ms-windows/xp_theme.c) loading libraries (wintab32.dll and uxtheme.dll) in an insecure manner. This can be exploited to load arbitrary libraries when an application using this library e.g. opens a file located on a remote WebDAV or SMB share.</p><p>Successful exploitation may allow execution of arbitrary code.</p><p>Solution Update to version 2.24.0.</p><p>Provided and/or discovered by JVN credits Naoto Katsumi, LAC Co., Ltd.</p><p>Original Advisory JVN: http://jvn.jp/en/jp/JVN58019849/index.html</p><p>GTK+: http://git.gnome.org/browse/gtk+/commit/modules/engines/ms-windows/xp_theme.c?h=gtk-2-24&amp;id=d6e11a97e318158f5d210a0476870dfe14ed95e6 http://git.gnome.org/browse/gtk+/commit/gdk/win32/gdkinput-win32.c?h=gtk-2-24&amp;id=88f54ea47d4a55bbbf9e34a7a0502f365eb69ae5&amp;ss=1</p><p>Deep Links Links available in Customer Area</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-secunia-psi" rel="tag" title="see questions tagged &#39;secunia-psi&#39;">secunia-psi</span> <span class="post-tag tag-link-vulnerability" rel="tag" title="see questions tagged &#39;vulnerability&#39;">vulnerability</span> <span class="post-tag tag-link-gtk+" rel="tag" title="see questions tagged &#39;gtk+&#39;">gtk+</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '11, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/3451ea1bfc589c036b1fd49b4a03cafb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reijken01&#39;s gravatar image" /><p><span>reijken01</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reijken01 has no accepted answers">0%</span></p></div></div><div id="comments-container-6181" class="comments-container"><span id="6192"></span><div id="comment-6192" class="comment"><div id="post-6192-score" class="comment-score"></div><div class="comment-text"><p>One problem is that the GTK+ project has stopped providing bundles. The latest available is 2.22 which i the one we use.</p></div><div id="comment-6192-info" class="comment-info"><span class="comment-age">(07 Sep '11, 09:17)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-6181" class="comment-tools"></div><div class="clear"></div><div id="comment-6181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6195"></span>

<div id="answer-container-6195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6195-score" class="post-score" title="current number of votes">0</div><span id="post-6195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like this issue was fixed in various branches in the GTK+ sources (including 2-16 and 2-22) on September 2, 2010. Wireshark 1.6 ships with files from <a href="http://ftp.gnome.org/pub/GNOME/binaries/win32/gtk+/2.22/"><code>gtk+-bundle_2.22.1-20101227_win32.zip</code></a>, which appears to be safe.</p><p>Wireshark 1.4 ships with files from <a href="http://ftp.gnome.org/pub/GNOME/binaries/win32/gtk+/2.16/"><code>gtk+-bundle_2.16.6-20100207_win32.zip</code></a>. This <a href="http://git.gnome.org/browse/gtk+/commit/modules/engines/ms-windows?h=gtk-2-16&amp;id=8c6b326d2e0c71eb801eb6480589621824ac48b6">predates the DLL hijacking fixes</a> but I can't duplicate the issue here using Process Monitor or HD Moore's PoC runcalc.dll. I'll update 1.4 to <code>gtk+-bundle_2.16.6-20100912_win32.zip</code>, which should contain the fix just to be safe.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-6195" class="comments-container"></div><div id="comment-tools-6195" class="comment-tools"></div><div class="clear"></div><div id="comment-6195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

