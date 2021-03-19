+++
type = "question"
title = "IOError while running wireshark from build directory for pyreshark"
description = '''Hi, I&#x27;m trying to build wireshark after building from pyreshark. When I run the command WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark I get the following error.  Can&#x27;t open Pyreshark init file: /home/paavu/wireshark-1.12.4/python/pyreshark.py  IOError: [Errno 2] No such file or directory: &#x27;/home/...'''
date = "2015-04-09T09:50:00Z"
lastmod = "2015-04-09T10:19:00Z"
weight = 41327
keywords = [ "ioerror", "pyreshark" ]
aliases = [ "/questions/41327" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IOError while running wireshark from build directory for pyreshark](/questions/41327/ioerror-while-running-wireshark-from-build-directory-for-pyreshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41327-score" class="post-score" title="current number of votes">0</div><span id="post-41327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to build wireshark after building from pyreshark. When I run the command <code>WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark</code></p><p>I get the following error.</p><pre><code> Can&#39;t open Pyreshark init file: /home/paavu/wireshark-1.12.4/python/pyreshark.py
    IOError: [Errno 2] No such file or directory: &#39;/home/paavu/wireshark-1.12.4/python/pyreshark.py&#39;</code></pre><p>The actual path of pyreshark.py is <code>wireshark-1.12.4/plugins/pyreshark/python/pyreshark.py</code></p><p>Any help is appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ioerror" rel="tag" title="see questions tagged &#39;ioerror&#39;">ioerror</span> <span class="post-tag tag-link-pyreshark" rel="tag" title="see questions tagged &#39;pyreshark&#39;">pyreshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '15, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/07e6cbcd9a14e42a4341db7ac250ba6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Praveen&#39;s gravatar image" /><p><span>Praveen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Praveen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '16, 15:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-41327" class="comments-container"></div><div id="comment-tools-41327" class="comment-tools"></div><div class="clear"></div><div id="comment-41327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41328"></span>

<div id="answer-container-41328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41328-score" class="post-score" title="current number of votes">0</div><span id="post-41328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to contact the Pyreshark plugin developer for that, see <a href="https://github.com/ashdnazg/pyreshark">https://github.com/ashdnazg/pyreshark</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '15, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41328" class="comments-container"></div><div id="comment-tools-41328" class="comment-tools"></div><div class="clear"></div><div id="comment-41328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

