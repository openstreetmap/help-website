+++
type = "question"
title = "error with make rpm-package for Wireshark-2.0.1 for command-line only option"
description = '''I wish to build a source rpm package but for only the command-line components of wirshark 2.0.1. Looking at previous queries this looked possible by first specifying &quot;--disable-wireshark&quot; for the configure script argument. This appears successful for the configure stage and when running just &quot;make&quot;....'''
date = "2016-01-08T08:10:00Z"
lastmod = "2016-01-08T09:54:00Z"
weight = 48975
keywords = [ "rpm-package", "command-line" ]
aliases = [ "/questions/48975" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error with make rpm-package for Wireshark-2.0.1 for command-line only option](/questions/48975/error-with-make-rpm-package-for-wireshark-201-for-command-line-only-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48975-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wish to build a source rpm package but for only the command-line components of wirshark 2.0.1. Looking at previous queries this looked possible by first specifying "--disable-wireshark" for the configure script argument. This appears successful for the configure stage and when running just "make".</p><p>However if I wish to use the provided rpm spec content and then run:</p><p>make rpm-package</p><p>this fails the configure check with :</p><p>configure: error: Neither Qt nor GTK+ 2.12.0 or later are available, so Wireshark can't be compiled</p><p>I have also tried modifying the spec so that all gui conditions options are excluded - e.g "%bcond_without qt " and can see this relected in makefile.in with: RPMBUILD_WITH_ARGS = --without gtk2 --without gtk3 --without qt --without qt5 --without lua</p><p>However the configure check fails before reading the spec. for the rpmbuild</p></div><div id="question-tags" class="tags-container tags">rpm-package command-line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '16, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/c0b0e8d7a282353b77705e5bf59a303d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="windymc&#39;s gravatar image" /><p>windymc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="windymc has no accepted answers">0%</span></p></div></div><div id="comments-container-48975" class="comments-container"></div><div id="comment-tools-48975" class="comment-tools"></div><div class="clear"></div><div id="comment-48975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48987"></span>

<div id="answer-container-48987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48987-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In general the RPM generation assumes you're <em>building</em> both the GUI and CLI. Once built you can install only the CLI but it's set up so you do actually have to build both.</p><p>If that's not possible (because the system you're compiling on doesn't have Qt nor Gtk) then you'll need to hack up the spec file. Keep in mind that <code>./configure</code> is run (again) within the spec file so you'll need to take out not only all the <code>%if %{with qt} || %{with qt5}</code> stuff but you'll also have to modify the <code>./configure</code> arguments to add "--disable-wireshark".</p><p>In other words when you (manually) run ./configure (before <code>make rpm-package</code>) only some of the options are passed in to the RPM generation; "--disable-wireshark" is not among them. (It would be possible to do that but it would be a-whole-nother layer of conditionals in the spec file; thus far that's looked like too much of a pain to me.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '16, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-48987" class="comments-container"><span id="49093"></span><div id="comment-49093" class="comment"><div id="post-49093-score" class="comment-score"></div><div class="comment-text"><p>As below, Had to do a bit a more work with the spec than just take out the qt &amp; gtk package sections and adding "--disable-wireshark". But have now built the source rpm so thanks for your help Jeff:-)</p><ol><li><p>"--disable-warnings-as-errors" parameter is not known so removed it .</p></li><li><p>And also rpmbuild fails with "could not find file" due to following: %exclude %{_bindir}/wireshark*</p></li></ol><p>%exclude %{_mandir}/man1/wireshark.* %exclude %{_datadir}/applications/wireshark-gtk.desktop</p><p>...so removed them. Even though the purpose of them is to say don't worry about including them, rpm logic has to verify that they exist and then exclude them !</p></div><div id="comment-49093-info" class="comment-info"><span class="comment-age">(11 Jan '16, 08:42)</span> windymc</div></div></div><div id="comment-tools-48987" class="comment-tools"></div><div class="clear"></div><div id="comment-48987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

