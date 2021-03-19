+++
type = "question"
title = "Building Latest Trunk"
description = '''Hi I get the follwing error during a build all, can somebidy help? Microsoft (R) Program Maintenance Utility Version 9.00.21022.08 Copyright (C) Microsoft Corporation. All rights reserved.   bison -d -p ascend ascend.y -o ascend.c  bash -o igncr ..&#92;tools&#92;runlex.sh &quot;flex&quot; -oascend_scanner.c ascend_sc...'''
date = "2010-09-16T08:32:00Z"
lastmod = "2010-09-16T15:20:00Z"
weight = 153
keywords = [ "sed", "build", "error" ]
aliases = [ "/questions/153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Building Latest Trunk](/questions/153/building-latest-trunk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-153-score" class="post-score" title="current number of votes">0</div><span id="post-153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I get the follwing error during a build all, can somebidy help?</p><pre><code>Microsoft (R) Program Maintenance Utility Version 9.00.21022.08
Copyright (C) Microsoft Corporation.  All rights reserved.

        bison  -d -p ascend ascend.y -o ascend.c
        bash -o igncr ..\tools\runlex.sh &quot;flex&quot; -oascend_scanner.c ascend_scanner.l
cygwin warning:
  MS-DOS style path detected: ..\tools\runlex.sh
  Preferred POSIX equivalent is: ../tools/runlex.sh
  CYGWIN environment variable option &quot;nodosfilewarning&quot; turns off this warning.
  Consult the user&#39;s guide for more details about POSIX paths:
    http://cygwin.com/cygwin-ug-net/using.html#using-pathnames
sed: 1: &quot;s/-o/(.*/)//1/&quot;: bad flag in substitute command: &#39;)&#39;</code></pre><p>thanks steve</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sed" rel="tag" title="see questions tagged &#39;sed&#39;">sed</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '10, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/321f94a2946c71a35e9704a06c7d71a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="penfold&#39;s gravatar image" /><p><span>penfold</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="penfold has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Sep '10, 11:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-153" class="comments-container"><span id="161"></span><div id="comment-161" class="comment"><div id="post-161-score" class="comment-score"></div><div class="comment-text"><p>Can you paste in the output of "nmake -f makefile.nmake verify_tools"? It might also help to run the lex command line by had with the "-x" flag:</p><pre><code>bash -x -o igncr ../tools/runlex.sh &quot;flex&quot; -oascend_scanner.c ascend_scanner.l</code></pre></div><div id="comment-161-info" class="comment-info"><span class="comment-age">(16 Sep '10, 15:20)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-153" class="comment-tools"></div><div class="clear"></div><div id="comment-153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

