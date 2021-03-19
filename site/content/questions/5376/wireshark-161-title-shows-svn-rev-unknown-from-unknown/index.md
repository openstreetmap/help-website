+++
type = "question"
title = "wireshark 1.6.1 - title shows &quot;SVN Rev Unknown from unknown&quot;"
description = '''I downloaded the source code and installed with the following settings:  tar -xjf wireshark-1.6.1.tar.bz2 cd wireshark-1.6.1 ./configure --prefix=/usr --enable-threads --with-lua --with-ssl --enable-setuid-install make make install  When I start wireshark, its title shows &quot;SVN Rev Unknown from unkno...'''
date = "2011-08-01T07:28:00Z"
lastmod = "2011-08-01T18:03:00Z"
weight = 5376
keywords = [ "development" ]
aliases = [ "/questions/5376" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark 1.6.1 - title shows "SVN Rev Unknown from unknown"](/questions/5376/wireshark-161-title-shows-svn-rev-unknown-from-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5376-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded the source code and installed with the following settings:</p><pre><code>tar -xjf wireshark-1.6.1.tar.bz2
cd wireshark-1.6.1
./configure --prefix=/usr --enable-threads --with-lua --with-ssl --enable-setuid-install
make
make install</code></pre><p>When I start wireshark, its title shows "SVN Rev Unknown from unknown". Although it is not a problem, does someone know why this happens?</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '11, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/e9b45c28c72381bf7634d0d8e95005cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="solohuang&#39;s gravatar image" /><p>solohuang<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="solohuang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '11, 16:09</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5376" class="comments-container"></div><div id="comment-tools-5376" class="comment-tools"></div><div class="clear"></div><div id="comment-5376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5380"></span>

<div id="answer-container-5380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5380-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like a bug.</p><p>Please file a bug report at bugs.wireshark.org</p><p>Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '11, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-5380" class="comments-container"><span id="5506"></span><div id="comment-5506" class="comment"><div id="post-5506-score" class="comment-score"></div><div class="comment-text"><p>As I mentioned in the comment to Jeff, I committed a change in r38340. But now I don't know if bug 1413 needs to be reopened and some other change made. I leave that to someone else at this point.</p></div><div id="comment-5506-info" class="comment-info"><span class="comment-age">(04 Aug '11, 13:48)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-5380" class="comment-tools"></div><div class="clear"></div><div id="comment-5380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5385"></span>

<div id="answer-container-5385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5385-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1413">bug 1413</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '11, 18:03</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5385" class="comments-container"><span id="5392"></span><div id="comment-5392" class="comment"><div id="post-5392-score" class="comment-score"></div><div class="comment-text"><p>Interesting. It was decided <em>long</em> ago that if the SVN version couldn't be determined (e.g., source built from tarball), "SVN Rev Unknown" would be shown instead of the actual revision number.</p><p>Probably not the place for this but: That "unknown" label is verbose and seemingly useless. It should've been omitted altogether.</p></div><div id="comment-5392-info" class="comment-info"><span class="comment-age">(01 Aug '11, 19:49)</span> helloworld</div></div><span id="5393"></span><div id="comment-5393" class="comment"><div id="post-5393-score" class="comment-score"></div><div class="comment-text"><p>Feel free to open a bug report and submit a proposed patch for some other solution. Be sure to keep in mind where SVNVERSION and SVNPATH are used, such as in capinfos.c, editcap.c, mergecap.c, text2pcap.c, version_info.c and possibly other places.</p></div><div id="comment-5393-info" class="comment-info"><span class="comment-age">(01 Aug '11, 19:58)</span> cmaynard ♦♦</div></div><span id="5496"></span><div id="comment-5496" class="comment"><div id="post-5496-score" class="comment-score"></div><div class="comment-text"><p>Shouldn't our official source tarballs, well, not try to use SVN and just report the version [especially now that we put the version in the titlebar]?</p></div><div id="comment-5496-info" class="comment-info"><span class="comment-age">(04 Aug '11, 06:32)</span> JeffMorriss ♦</div></div><span id="5505"></span><div id="comment-5505" class="comment"><div id="post-5505-score" class="comment-score"></div><div class="comment-text"><p>Yes, I think so. I committed a change in r38340 and scheduled it for 1.6.2 and 1.4.9. Essentially, it reverts the change I made for bug 1413 ... but now I don't now if bug 1413 needs to be reopened. If it does, I guess I'll let someone else try to come up with a fix for it.</p></div><div id="comment-5505-info" class="comment-info"><span class="comment-age">(04 Aug '11, 13:45)</span> cmaynard ♦♦</div></div><span id="6202"></span><div id="comment-6202" class="comment"><div id="post-6202-score" class="comment-score"></div><div class="comment-text"><p>I finally got back to this and committed a different change in r38933. I'll schedule that for 1.6.3 once the queue for that release opens. (Chris' change in 38340 made 1.6.2 so users of the source tarballs shouldn't notice any change between 1.6.2 and 1.6.3.)</p></div><div id="comment-6202-info" class="comment-info"><span class="comment-age">(07 Sep '11, 19:00)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-5385" class="comment-tools"></div><div class="clear"></div><div id="comment-5385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

