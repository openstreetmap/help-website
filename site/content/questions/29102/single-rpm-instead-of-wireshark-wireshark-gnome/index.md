+++
type = "question"
title = "Single RPM instead of wireshark &amp; wireshark-gnome?"
description = '''Hi all, I am building from the 1.10 branch for the first time and noticed that the included spec file in this release generates two RPMs like Red Hat normally does with their OS&#x27; releases for Wireshark.  I&#x27;m looking to have a single RPM for ease of installations. The last time I built an RPM was fro...'''
date = "2014-01-22T10:41:00Z"
lastmod = "2014-01-22T11:51:00Z"
weight = 29102
keywords = [ "rpm", "redhat" ]
aliases = [ "/questions/29102" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Single RPM instead of wireshark & wireshark-gnome?](/questions/29102/single-rpm-instead-of-wireshark-wireshark-gnome)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29102-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am building from the 1.10 branch for the first time and noticed that the included spec file in this release generates two RPMs like Red Hat normally does with their OS' releases for Wireshark.</p><p>I'm looking to have a single RPM for ease of installations. The last time I built an RPM was from 1.8.x and it still had a single RPM. I am somewhat spec "literate" and think it wouldn't be too difficult to make the required changes, but then again there is a lot more content in the new spec file compared to this older one and I am a bit unsure of any chronological dependencies that might come into play if I started combining, for example the "%install" and "%install gnome" sections.</p><p>Before I get started, wondering if there is a ./configure option or something similar that automatically generates a spec file for a single RPM?</p><p>Thanks for reading, J</p></div><div id="question-tags" class="tags-container tags">rpm redhat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/34ab7b09251ce1194b33bb66c2b32d17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorwex&#39;s gravatar image" /><p>jorwex<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorwex has no accepted answers">0%</span></p></div></div><div id="comments-container-29102" class="comments-container"><span id="29103"></span><div id="comment-29103" class="comment"><div id="post-29103-score" class="comment-score"></div><div class="comment-text"><p>More info. I see this in the changelog for the spec:</p><ul><li>Mon Feb 6 2013 Jeff Morriss **- Overhaul to make this file more useful/up to date. Many changes are based on Fedora's .spec file. Changes include:<ul><li>Create a separate wireshark-gnome package (like Redhat).**</li><li>Control some things with variables set at the top of the file.</li><li>Allow the user to configure how dumpcap is installed.</li><li>Allow the user to choose some options including GTK2 or GTK3.</li><li>Greatly expand the BuildRequires entries; get the minimum versions of some things from 'configure'.</li><li>Install freedesktop files for better (free)desktop integration.</li></ul></li></ul></div><div id="comment-29103-info" class="comment-info"><span class="comment-age">(22 Jan '14, 10:59)</span> jorwex</div></div><span id="29107"></span><div id="comment-29107" class="comment"><div id="post-29107-score" class="comment-score"></div><div class="comment-text"><p>I removed the comment that Jeff is responding to (I had it earlier here) because I thought it was worthy of a separate post: <a href="http://ask.wireshark.org/questions/29106/different-so-dependencies-between-normal-build-and-rpm">http://ask.wireshark.org/questions/29106/different-so-dependencies-between-normal-build-and-rpm</a></p></div><div id="comment-29107-info" class="comment-info"><span class="comment-age">(22 Jan '14, 12:10)</span> jorwex</div></div></div><div id="comment-tools-29102" class="comment-tools"></div><div class="clear"></div><div id="comment-29102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29105"></span>

<div id="answer-container-29105" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29105-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The reason for the package separation is both to support installing tshark on machines without GTK/X and to allow for the eventual migration to a Qt GUI (the development version now has 3 RPMs: wireshark, wireshark-gnome, and wireshark-qt: you can install either, both, or neither of the GUIs).</p><p>No, there isn't an option to go back to the one-RPM version. You're right it should be possible to hack it up to work but then you'd have to redo that work again in the next stable version because a lot changed to support the Qt GUI package. There was another user who was having some problems and eventually went back and just used the 1.8 spec file--and reported success in doing so. Not that I'd really encourage you to do that...</p><p>Is there a particular reason you really need one RPM file?</p><p>As for the libwiretap.so.2 problem: that sounds vaguely familiar but I thought it was fixed. Do you have a Wireshark installed which supplies libwiretap.so.2? If you do, the workaround is probably to remove that installed version before building your RPM. But I really thought we fixed that... Need to do some research (no promises--I'm quite short on time these days). (And actually the machine where I build my 1.10 RPMs has Wireshark 1.8 installed, that package supplies libwiretap.so.2, and my packages build just fine. Hmm...)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-29105" class="comments-container"><span id="29108"></span><div id="comment-29108" class="comment"><div id="post-29108-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info!</p><p>No great reason for the single rpm. I think I can live with it.<br />
</p><p>Wow I had the Red Hat el6-supplied 1.2.x installed on the build machine. Trying build again now that I have removed it...</p></div><div id="comment-29108-info" class="comment-info"><span class="comment-age">(22 Jan '14, 12:14)</span> jorwex</div></div><span id="29109"></span><div id="comment-29109" class="comment"><div id="post-29109-score" class="comment-score"></div><div class="comment-text"><p>WORKED! You are awesome Jeff! That bug must still remain somehow.</p></div><div id="comment-29109-info" class="comment-info"><span class="comment-age">(22 Jan '14, 12:15)</span> jorwex</div></div><span id="29113"></span><div id="comment-29113" class="comment"><div id="post-29113-score" class="comment-score"></div><div class="comment-text"><p>OK I found the fix I was thinking of (r48582) and it is fixed in the 1.10 series (see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6011">bug 6011</a>). So I'm not sure what's going on with your libwiretap problem...</p></div><div id="comment-29113-info" class="comment-info"><span class="comment-age">(22 Jan '14, 13:55)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-29105" class="comment-tools"></div><div class="clear"></div><div id="comment-29105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

