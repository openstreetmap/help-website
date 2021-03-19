+++
type = "question"
title = "How do I correct this problem with verify_tools?"
description = '''I want build wireshark 1.7.0, but get the following output from the verify_tools step:  Z:&#92;wireshark&amp;gt;nmake -f Makefile.nmake verify_tools  Microsoft (R) 程序维护实用工具 9.00.30729.01 版 版权所有(C) Microsoft Corporation。保留所有权利。  : No such file or directory8: /cygdrive/z/wireshark/tools/win-setup.sh  : cannot...'''
date = "2012-01-12T08:51:00Z"
lastmod = "2013-12-20T08:33:00Z"
weight = 8344
keywords = [ "development", "build" ]
aliases = [ "/questions/8344" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I correct this problem with verify\_tools?](/questions/8344/how-do-i-correct-this-problem-with-verify_tools)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8344-score" class="post-score" title="current number of votes">0</div><span id="post-8344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want build wireshark 1.7.0, but get the following output from the <code>verify_tools</code> step:</p><pre><code>Z:\wireshark&gt;nmake -f Makefile.nmake verify_tools

Microsoft (R) 程序维护实用工具 9.00.30729.01 版
版权所有(C) Microsoft Corporation。保留所有权利。

: No such file or directory8: /cygdrive/z/wireshark/tools/win-setup.sh

: cannot execute: No such file or directoryve/z/wireshark/tools/win-setup.sh

: No such file or directory8: /cygdrive/z/wireshark/tools/win-setup.sh

: cannot execute: No such file or directoryve/z/wireshark/tools/win-setup.sh

NMAKE : fatal error U1077: “D:\cygwin\bin\bash.EXE”: 返回代码“0x7e”
Stop.</code></pre><p>...and I can find the file here:</p><pre><code>Z:\wireshark&gt;pwd
/cygdrive/z/wireshark

Z:\wireshark&gt;ls tools/win-setup.sh
tools/win-setup.sh</code></pre><p>How can I fix this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '12, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/1781217b8788ee26bdee4b0220f22174?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huanglihao&#39;s gravatar image" /><p><span>huanglihao</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huanglihao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '12, 09:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8344" class="comments-container"><span id="8351"></span><div id="comment-8351" class="comment"><div id="post-8351-score" class="comment-score"></div><div class="comment-text"><p>verify_tools first calls <code>tools/win32-setup.sh</code> (or <code>win64-setup.sh</code>) which in turn calls <code>win-setup.sh</code>.</p><p><code>win32-setup.sh</code> is being found and executed OK.</p><pre><code>win32-setup.sh

...

WIN_SETUP=`echo $0 | sed -e s/win32/win/

exec $WIN_SETUP [email protected]</code></pre><p>I expect there's some problem with the above (maybe related to your specific language environment ?).</p><p>Are you comfortable with doing a little debugging ?</p><p>Specifically: add something like <code>printf "&gt;%s&lt;\n", $WIN_SETUP</code> just before the <code>exec</code> in <code>win32-setup.sh</code> and rerun the <code>verify-tools</code>.</p></div><div id="comment-8351-info" class="comment-info"><span class="comment-age">(12 Jan '12, 09:39)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="28307"></span><div id="comment-28307" class="comment"><div id="post-28307-score" class="comment-score"></div><div class="comment-text"><p>I know this is old but did you ever fix this issue? Im having the same problem and cant figure it out</p></div><div id="comment-28307-info" class="comment-info"><span class="comment-age">(20 Dec '13, 08:33)</span> <span class="comment-user userinfo">Hockeyfreak889</span></div></div></div><div id="comment-tools-8344" class="comment-tools"></div><div class="clear"></div><div id="comment-8344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

