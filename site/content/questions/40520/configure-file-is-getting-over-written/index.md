+++
type = "question"
title = "Configure file is getting over written"
description = '''Hi all We are trying to build Wireshark RPM package with a different package name. In order to do this we have modified the following files.  configure configure.ac wireshark.spec.in  Once the changes are done, we are performing ./configure which goes fine and then we are doing make. Once we do the ...'''
date = "2015-03-12T12:41:00Z"
lastmod = "2015-03-13T13:58:00Z"
weight = 40520
keywords = [ "configure" ]
aliases = [ "/questions/40520" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Configure file is getting over written](/questions/40520/configure-file-is-getting-over-written)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40520-score" class="post-score" title="current number of votes">0</div><span id="post-40520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>We are trying to build Wireshark RPM package with a different package name. In order to do this we have modified the following files.</p><ul><li>configure</li><li>configure.ac</li><li>wireshark.spec.in</li></ul><p>Once the changes are done, we are performing ./configure which goes fine and then we are doing make. Once we do the make we are observing that it is regenerating configure file. All the changes done by us in configure file is partially overwritten. We want to know why is this happening and how to control it. Following couple of lines are observed when we do make.</p><p><code># make  CDPATH="${ZSH_VERSION+.}:" &amp;&amp; cd . &amp;&amp; /bin/sh /home/KIRAN/ABCDEFG-5.0/missing --run aclocal-1.11</code>./aclocal-flags<code>cd . &amp;&amp; /bin/sh /home/KIRAN/ABCDEFG-5.0/missing --run automake-1.11 --gnu  CDPATH="${ZSH_VERSION+.}:" &amp;&amp; cd . &amp;&amp; /bin/sh /home/KIRAN/ABCDEFG-5.0/missing --run autoconf  /bin/sh ./config.status --recheck</code></p><p>Please let us know what is reason the above 2 lines are being executed by make. Thanks in advance.</p><p>Regards Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-configure" rel="tag" title="see questions tagged &#39;configure&#39;">configure</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '15, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p><span>Kiran Kumar G</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Mar '15, 02:12</strong> </span></p></div></div><div id="comments-container-40520" class="comments-container"></div><div id="comment-tools-40520" class="comment-tools"></div><div class="clear"></div><div id="comment-40520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40543"></span>

<div id="answer-container-40543" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40543-score" class="post-score" title="current number of votes">0</div><span id="post-40543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kiran Kumar G has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Please let us know what is reason the above 2 lines are being executed by make</p></blockquote><p>Because that's how automake-based projects work; they re-generate the configure script if the source files for it (configure.ac, acinclude.m4) are newer than the generated configure script. They do so under the assumption that the configure script is purely generated from configure.ac and acinclude.m4 and <strong><em>NOT</em></strong> edited manually by the user; do not <strong><em>EVER</em></strong> violate that assumption by modifying configure by hand - <strong><em>ALWAYS</em></strong> edit <strong><em>ONLY</em></strong> the configure.ac and/or acinclude.m4 files, and then run make. The Makefile will, when you run make re-generate the configure script for you, if necessary, with the commands you showed.</p><p>Wireshark uses automake, so that's how it works.</p><p>Again, <strong><em>DO NOT</em></strong> make <strong><em>ANY</em></strong> changes to the configure script yourself. Edit <strong><em>ONLY</em></strong> configure.ac and, if necessary, acinclude.m4, and then run make. (Do not edit aclocal.m4, either; it's generated from acinclude.m4, and make should regenerate that, as well, by running automake.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '15, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40543" class="comments-container"></div><div id="comment-tools-40543" class="comment-tools"></div><div class="clear"></div><div id="comment-40543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

