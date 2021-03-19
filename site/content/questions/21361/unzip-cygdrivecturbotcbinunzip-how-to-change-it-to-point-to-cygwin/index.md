+++
type = "question"
title = "unzip: /cygdrive/c/Turbo/TC/BIN/unzip.. How to change it to point to cygwin"
description = '''Hi, when I run nmake -f Makefile.namke verify_tools, unzip package is currently pointing to   unzip: /cygdrive/c/Turbo/TC/BIN/unzip  Because of which I&#x27;m getting following err while running nmake -f Makefile.nmake setup  ERROR: Couldn&#x27;t unpack &#x27;/cygdrive/c/Wireshark-win32-libs/gtk+-bundle_2.24.14-1....'''
date = "2013-05-21T17:02:00Z"
lastmod = "2013-05-22T01:42:00Z"
weight = 21361
keywords = [ "development", "build", "plugin" ]
aliases = [ "/questions/21361" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unzip: /cygdrive/c/Turbo/TC/BIN/unzip.. How to change it to point to cygwin](/questions/21361/unzip-cygdrivecturbotcbinunzip-how-to-change-it-to-point-to-cygwin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21361-score" class="post-score" title="current number of votes">0</div><span id="post-21361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>when I run nmake -f Makefile.namke verify_tools, unzip package is currently pointing to</p><pre><code>   unzip: /cygdrive/c/Turbo/TC/BIN/unzip</code></pre><p>Because of which I'm getting following err while running nmake -f Makefile.nmake setup</p><pre><code>   ERROR: Couldn&#39;t unpack &#39;/cygdrive/c/Wireshark-win32-libs/gtk+-bundle_2.24.14-1.1_win32ws.zip&#39;

   NMAKE : fatal error U1077: &#39;c:\cygwin\bin\bash.EXE&#39; : return code &#39;0x1&#39;
   Stop.</code></pre><p>I have included cygwin (C:\cygwin\bin) in my path env variable. I also can see unzip is being installed in /usr/bin/unzip.exe. So, I wanted to know how I can change it to point to /usr/bin/unzip Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '13, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/1d8e93e282588309b50b28244614c739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiremeup&#39;s gravatar image" /><p><span>wiremeup</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiremeup has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 May '13, 17:03</strong> </span></p></div></div><div id="comments-container-21361" class="comments-container"></div><div id="comment-tools-21361" class="comment-tools"></div><div class="clear"></div><div id="comment-21361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21367"></span>

<div id="answer-container-21367" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21367-score" class="post-score" title="current number of votes">1</div><span id="post-21367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have an entry in your path that points to the TurboC bin directory. There is no need to add Cygwin to your path, the Wireshark build environment does that for you.</p><p>To fix the issue, either modify your user or system path as appropriate to remove the entry for the TurboC bin directory (this may break TurboC though) or in the command shell you use to compile Wireshark modify the PATH environment variable so that the TurboC bin directory is not listed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '13, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '13, 01:54</strong> </span></p></div></div><div id="comments-container-21367" class="comments-container"><span id="21368"></span><div id="comment-21368" class="comment"><div id="post-21368-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer.. but I added cygwin/bin to the beginning of the PATH variable, before TurboC/bin directory, after which it worked...!! Thanks for your time...</p></div><div id="comment-21368-info" class="comment-info"><span class="comment-age">(22 May '13, 01:42)</span> <span class="comment-user userinfo">wiremeup</span></div></div></div><div id="comment-tools-21367" class="comment-tools"></div><div class="clear"></div><div id="comment-21367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

