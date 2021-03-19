+++
type = "question"
title = "Error: Failed build dependencies while making Deb"
description = '''Hi all, I&#x27;m trying to build Debian-package in Ubuntu by using  $./configure $ make debian-package  but unfortunately, I got an error with gtk like this:  ERROR: ld.so: object &#x27;libfakeroot-sysv.so&#x27; from LD_PRELOAD cannot be preloaded: ignored. dpkg-shlibdeps: error: no dependency information found fo...'''
date = "2013-09-18T23:31:00Z"
lastmod = "2013-09-19T01:22:00Z"
weight = 24940
keywords = [ "dependencies", "debian" ]
aliases = [ "/questions/24940" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error: Failed build dependencies while making Deb](/questions/24940/error-failed-build-dependencies-while-making-deb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24940-score" class="post-score" title="current number of votes">0</div><span id="post-24940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm trying to build Debian-package in Ubuntu by using</p><pre><code>$./configure
$ make debian-package</code></pre><p>but unfortunately, I got an error with gtk like this:</p><pre><code>ERROR: ld.so: object &#39;libfakeroot-sysv.so&#39; from LD_PRELOAD cannot be preloaded: ignored.
dpkg-shlibdeps: error: no dependency information found for /usr/local/lib/libgdk-3.so.0 (used by debian/wireshark/usr/bin/wireshark)
dh_shlibdeps: dpkg-shlibdeps -Tdebian/wireshark.substvars debian/wireshark/usr/bin/wireshark returned exit code 2
make[1]: *** [binary-arch] Error 2
make[1]: Leaving directory `/media/sonnh/Win7_x64/wireshark&#39;
dpkg-buildpackage: error: fakeroot debian/rules binary gave error exit status 2
make: *** [debian-package] Error 2</code></pre><p>I searched on Internet and it seems that many people got the similar errors. Some of them ignore the problem by skipping the process of dependencies checking but I think it is not a good way. Could you please give me any idea to pass over this case? I can run <code>"make"</code> or <code>"make install"</code> successfully but to generate Deb. file, it is impossible. I'm sure that gtk+3 installed (otherwise, it cannot run ./configure successfully). So, What should I do ? Thanks for your help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dependencies" rel="tag" title="see questions tagged &#39;dependencies&#39;">dependencies</span> <span class="post-tag tag-link-debian" rel="tag" title="see questions tagged &#39;debian&#39;">debian</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '13, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '13, 01:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-24940" class="comments-container"></div><div id="comment-tools-24940" class="comment-tools"></div><div class="clear"></div><div id="comment-24940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24946"></span>

<div id="answer-container-24946" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24946-score" class="post-score" title="current number of votes">0</div><span id="post-24946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It works perfectly well on my Ubuntu 13.04 (plain installation with the required dependencies). As I mentioned in your other question, you are building the code on a mounted NTFS drive (C:\ mounted to /media/sonnh/Win7_x64) and that may cause problems (due to NTFS!?!). As I already suggested: Try to build everything in a Linux filesystem like /var/tmp/wireshark.</p><p>As it works on my system, it is either related to</p><ul><li>the filesystem</li><li>some packages you did or did not install</li></ul><p>Here is what I did.</p><ul><li>Install Ubuntu 13.04 Desktop</li><li>apt-get update</li><li>apt-get upgrade</li><li>apt-get build-dep wireshark</li><li>apt-get install fakeroot</li><li>apt-get install dpatch</li><li>apt-get install python-support</li><li>apt-get install libgtk-3-dev</li><li>./configure</li><li>./make debian-package</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '13, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24946" class="comments-container"></div><div id="comment-tools-24946" class="comment-tools"></div><div class="clear"></div><div id="comment-24946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

