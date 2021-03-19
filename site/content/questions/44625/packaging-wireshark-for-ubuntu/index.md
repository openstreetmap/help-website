+++
type = "question"
title = "Packaging Wireshark for Ubuntu"
description = '''Hi guys, I am trying to package my Wireshark code for Ubuntu. I used the dpkg-buildpackage command which game me errors.Initially I got error with dh_quilt_unpatch returning error.So I commented out --with-quilt in rules files. Then I got an error saying no dependency information found for libz.so.1...'''
date = "2015-07-30T03:56:00Z"
lastmod = "2015-08-03T22:24:00Z"
weight = 44625
keywords = [ "packaging", "wireshark", "ubuntu" ]
aliases = [ "/questions/44625" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packaging Wireshark for Ubuntu](/questions/44625/packaging-wireshark-for-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44625-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I am trying to package my Wireshark code for Ubuntu. I used the dpkg-buildpackage command which game me errors.Initially I got error with dh_quilt_unpatch returning error.So I commented out --with-quilt in rules files. Then I got an error saying no dependency information found for libz.so.1 so I added</p><p><code>override_dh_shlibdeps:     dh_shlibdeps --dpkg-shlibdeps-params=--ignore-missing-info</code></p><p>and the build continues and completes.Now I have a few .deb files.My question now is</p><ul><li>Will there be any consequences of me commenting out quilt and overriding dependency information later while installing Wireshark?</li><li>Is there are way I can build it further into a single deb file or should I install them separately using dpkg (ofcourse I can use a script) but should I install them separately?</li></ul><p>Thanks for the help!</p><p>-koundi</p></div><div id="question-tags" class="tags-container tags">packaging wireshark ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Aug '15, 00:21</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-44625" class="comments-container"><span id="44629"></span><div id="comment-44629" class="comment"><div id="post-44629-score" class="comment-score"></div><div class="comment-text"><p>Wireshark version?</p></div><div id="comment-44629-info" class="comment-info"><span class="comment-age">(30 Jul '15, 05:39)</span> Jaap ♦</div></div><span id="44667"></span><div id="comment-44667" class="comment"><div id="post-44667-score" class="comment-score"></div><div class="comment-text"><p>@Jaap I am using the latest master-1.12 from git so its 1.12.6 I think right?</p></div><div id="comment-44667-info" class="comment-info"><span class="comment-age">(30 Jul '15, 22:42)</span> koundi</div></div><span id="44814"></span><div id="comment-44814" class="comment"><div id="post-44814-score" class="comment-score"></div><div class="comment-text"><p>What platform do you develop on? Debian squeeze / wheezy / jessie / sid? Or Ubuntu something?</p></div><div id="comment-44814-info" class="comment-info"><span class="comment-age">(04 Aug '15, 02:36)</span> Jaap ♦</div></div><span id="44849"></span><div id="comment-44849" class="comment"><div id="post-44849-score" class="comment-score"></div><div class="comment-text"><p>I use UBUNTU 14.04 for development and testing. I installed dpkg and few other debian packages to build the binaries. I did it once and that was 1.12.3 then I had just the libz problem.This quilt problem is new.</p></div><div id="comment-44849-info" class="comment-info"><span class="comment-age">(04 Aug '15, 22:49)</span> koundi</div></div><span id="44853"></span><div id="comment-44853" class="comment"><div id="post-44853-score" class="comment-score"></div><div class="comment-text"><p>Adapted the title/text accordingly.</p><p>Anyone running Ubuntu care to comment? I'm running Debian testing only.</p></div><div id="comment-44853-info" class="comment-info"><span class="comment-age">(05 Aug '15, 00:22)</span> Jaap ♦</div></div><span id="44901"></span><div id="comment-44901" class="comment not_top_scorer"><div id="post-44901-score" class="comment-score"></div><div class="comment-text"><p>@Jaap Thanks!</p></div><div id="comment-44901-info" class="comment-info"><span class="comment-age">(06 Aug '15, 01:13)</span> koundi</div></div></div><div id="comment-tools-44625" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-44625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44808"></span>

<div id="answer-container-44808" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44808-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Removing --with-quilt stops dh from applying Debian specific patches found in debian/patches. It might be that you've either polluted the tree with a broken build or have interfering changes in tree. If so you could clean the tree before starting the build, or maybe incorporate your changes in the <a href="http://pkg-perl.alioth.debian.org/howto/quilt.html">quilt</a></p><p>As for the problems with libz.so.1 I can see no obvious reason. You should have the libz-dev package for the build, I guess.</p><p>If you want to create a mother of debs for wireshark need to rework the control file and the package definition files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44808" class="comments-container"><span id="44812"></span><div id="comment-44812" class="comment"><div id="post-44812-score" class="comment-score"></div><div class="comment-text"><p>@Jaap Hi Thanks for the response. I haven't changed anything related to quilt.I have made some code changes in the existing dissectors.I have added a header file and that is it. I just type make debian-package and I got the error related to quilt.I do understand it is not the correct way to do things but I had to find a solution.Also can you elaborate on "incorporate changes in the quilt"? As far as the mother of debs is concerned I am fine with the way it is right now I just wanted to confirm that this is how it was intended to be and it has not happened because of the changes I made to the build process.</p></div><div id="comment-44812-info" class="comment-info"><span class="comment-age">(04 Aug '15, 00:56)</span> koundi</div></div><span id="44813"></span><div id="comment-44813" class="comment"><div id="post-44813-score" class="comment-score"></div><div class="comment-text"><p>also It installs properly on my machine and all the changes I made a working fine without any warnings or hiccups! Can you help me with the building it without making all these changes? Thanks a lot for the help! -koundi</p></div><div id="comment-44813-info" class="comment-info"><span class="comment-age">(04 Aug '15, 00:58)</span> koundi</div></div></div><div id="comment-tools-44808" class="comment-tools"></div><div class="clear"></div><div id="comment-44808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

