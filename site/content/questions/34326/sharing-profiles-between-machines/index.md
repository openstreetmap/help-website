+++
type = "question"
title = "sharing Profiles between machines"
description = '''I&#x27;d like to copy my collection of Profiles from my main machine to all the other machines where I run Wireshark (home, office, laptops, VMs ...) And I&#x27;ve done that -- copied it to an OS X laptop. Wireshark loads ... but the Profile menu in the lower right-hand corner isn&#x27;t visible. And when I start ...'''
date = "2014-07-01T11:45:00Z"
lastmod = "2014-07-10T15:51:00Z"
weight = 34326
keywords = [ "windows", "osx", "share", "profiles", "linux" ]
aliases = [ "/questions/34326" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [sharing Profiles between machines](/questions/34326/sharing-profiles-between-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to copy my collection of Profiles from my main machine to all the other machines where I run Wireshark (home, office, laptops, VMs ...)</p><p>And I've done that -- copied it to an OS X laptop.</p><p>Wireshark loads ... but the Profile menu in the lower right-hand corner isn't visible. And when I start capturing, I can see nothing but the top menu bar: no packets scrolling by ... I can access the menus, stop and restart capture and so forth, but at no time do I see packets ... the Wireshark window displays a dismal, uniform grey, with no features anywhere, other than the menu choices at the top.</p><p>I've tried converting the contents of ~/.wireshark as follows: cd .wireshark find . | xargs dos2unix</p><p>No change in Wireshark GUI behavior.</p><p>I've tried reverting to the original .wireshark folder, then copying a single Profile over. That works ... Wireshark remains functional ... but as soon as I select that profile and start capturing, I return to the 'dismal grey screen'.</p><p>Is anyone else sharing Profiles between different operating systems?</p><p>--sk</p><p>Stuart Kendrick</p></div><div id="question-tags" class="tags-container tags">windows osx share profiles linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '14, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p>skendric<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div></div><div id="comments-container-34326" class="comments-container"><span id="34327"></span><div id="comment-34327" class="comment"><div id="post-34327-score" class="comment-score"></div><div class="comment-text"><p>Are the Wireshark versions the same across your machines? Are the OSes the same? Have you tried restarting Wireshark after changing a profile? Also, note that 1.11.x versions would <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9463">crash</a> upon switching profiles (not sure if this also applied to 1.10.x), this is fixed in 1.12.x.</p></div><div id="comment-34327-info" class="comment-info"><span class="comment-age">(01 Jul '14, 13:08)</span> Lekensteyn</div></div><span id="34329"></span><div id="comment-34329" class="comment"><div id="post-34329-score" class="comment-score"></div><div class="comment-text"><ul><li>Yes, I'm using the same version of Wireshark (1.10.8) on both boxes</li><li>I quit Wireshark on both boxes before performing this copy</li><li>This phenomenon is sticky, in that having witnessed it, I can quit &amp; restart Wireshark multiple times and continue to observe the same behavior</li></ul></div><div id="comment-34329-info" class="comment-info"><span class="comment-age">(01 Jul '14, 14:20)</span> skendric</div></div><span id="34332"></span><div id="comment-34332" class="comment"><div id="post-34332-score" class="comment-score"></div><div class="comment-text"><p>Regarding the <em>'dismal grey screen'</em>, can you check your preferences to see if you have "Update list of packets in real time" disabled? (It's under <code>Edit -&gt; preferences -&gt; Capture</code>). It seems like it might be disabled.</p><p>Other than that, you might want to check your preferences file and see which gui.* preferences have been changed from their default settings that might be causing the problem. (If a preference is set to its default value, it will be commented via <code>#</code>.) If possible, post your preference file, or at least the non-default preferences, so that someone can try to recreate what you're experiencing.</p></div><div id="comment-34332-info" class="comment-info"><span class="comment-age">(01 Jul '14, 15:20)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-34326" class="comment-tools"></div><div class="clear"></div><div id="comment-34326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34589"></span>

<div id="answer-container-34589" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34589-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, your pointer to the gui.* preferences has helped me make progress.</p><p>When I unzip my .wireshark.tar.gz file, I get ../profiles/{whatever}/recent files of course. They start out looking like this (I've deleted the comment lines for ease-of-reading):</p><p>gui.toolbar_main_show: TRUE gui.filter_toolbar_show: TRUE gui.wireless_toolbar_show: FALSE gui.airpcap_driver_check_show: TRUE gui.packet_list_show: TRUE gui.tree_view_show: TRUE gui.byte_view_show: TRUE gui.statusbar_show: TRUE gui.packet_list_colorize: TRUE</p><p>OK, now I run Wireshark, select one of my profiles (ARP), and whoom, I see this dismal grey screen. Open ../profile/ARP/recent ... and I see the following:</p><p>gui.toolbar_main_show: FALSE gui.filter_toolbar_show: FALSE gui.wireless_toolbar_show: FALSE gui.airpcap_driver_check_show: FALSE gui.packet_list_show: FALSE gui.tree_view_show: FALSE gui.byte_view_show: FALSE gui.statusbar_show: FALSE gui.packet_list_colorize: FALSE</p><p>If I quit Wireshark, change FALSE to TRUE, then re-open Wireshark, I see a normal screen, complete with toolbars and packet lists and so forth.</p><p>And if I then switch to Default then back to ARP ... works fine -- those TRUE strings stay TRUE.</p><p>That being said, I'm still not seeing my customized columns nor Filters ... although I can clearly see them in ../profiles/{whatever}/preferences</p><p>[...]</p><p>OK, after some futzing, I'm going to claim that the problem relates to line termination. Here is the sequence of steps I need to take to get this to work:</p><p>rm -rf .wireshark tar xvf wireshark-preferences.zip cd .wireshark find . | xargs dos2unix</p><p>And then I'm fine -- no 'dismal grey screen', customized columns are visible, customized Filters are visible, things look peachy.</p><p>I have filed Bug 10272 to propose enhancing Wireshark under OS X to be agnostic to line termination characters. [Wireshark under Linux is already agnostic -- I can copy .wireshark there without trouble.]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '14, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p>skendric<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div></div><div id="comments-container-34589" class="comments-container"></div><div id="comment-tools-34589" class="comment-tools"></div><div class="clear"></div><div id="comment-34589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

