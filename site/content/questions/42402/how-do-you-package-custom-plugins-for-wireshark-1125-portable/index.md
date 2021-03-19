+++
type = "question"
title = "How do you package custom plugins for Wireshark 1.12.5 Portable?"
description = '''According to Wireshark documentation I&#x27;ve read, no further modifications is required to package Wireshark Portable (using &quot;packaging_papps&quot;). As of v1.12.5, I&#x27;m finding that, even though all custom plugins are included when creating a standard installer, only the default plugins are packaged for the...'''
date = "2015-05-14T13:37:00Z"
lastmod = "2015-05-15T07:40:00Z"
weight = 42402
keywords = [ "packaging", "wireshark", "portable", "plugin" ]
aliases = [ "/questions/42402" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do you package custom plugins for Wireshark 1.12.5 Portable?](/questions/42402/how-do-you-package-custom-plugins-for-wireshark-1125-portable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42402-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to Wireshark documentation I've read, no further modifications is required to package Wireshark Portable (using "packaging_papps"). As of v1.12.5, I'm finding that, even though all custom plugins are included when creating a standard installer, only the default plugins are packaged for the PortableApps.com version.</p><p>Help on ways to investigate this will be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">packaging wireshark portable plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '15, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p>coloncm<br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 May '16, 07:25</p></div></div><div id="comments-container-42402" class="comments-container"><span id="42414"></span><div id="comment-42414" class="comment"><div id="post-42414-score" class="comment-score"></div><div class="comment-text"><p>Perhaps, someone can explain what the line "!addplugindir "${EXTRA_PLUGINS}" is doing in Installer.nsi?</p></div><div id="comment-42414-info" class="comment-info"><span class="comment-age">(15 May '15, 07:12)</span> coloncm</div></div></div><div id="comment-tools-42402" class="comment-tools"></div><div class="clear"></div><div id="comment-42402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42417"></span>

<div id="answer-container-42417" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42417-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you closely follow the various <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=doc;h=b0babda2ba15a4f572730e3c39ab35d460b66216;hb=HEAD">README</a> files (at the very least, <code>README.developer</code>, <code>README.dissector</code> and <code>README.plugin</code>) as well as the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Wireshark developer's guide</a>, you should be able to successfully compile and package your plugins without having to do anything else.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '15, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-42417" class="comments-container"><span id="42419"></span><div id="comment-42419" class="comment"><div id="post-42419-score" class="comment-score"></div><div class="comment-text"><p>I have no problems with the custom plugins on standard packaging (Windows Installers). It is with the PortableApps package in that it's not including the custom plugins. Will it have anything to do with the use/inclusion of a custom_plugins.txt file instead of literally listing them on the Section "Dissector plugins" of the Wireshark.nsi file?</p></div><div id="comment-42419-info" class="comment-info"><span class="comment-age">(15 May '15, 08:06)</span> coloncm</div></div><span id="42420"></span><div id="comment-42420" class="comment"><div id="post-42420-score" class="comment-score"></div><div class="comment-text"><p>Possibly. Mine are still listed directly in the <code>wireshark.nsi</code> file because they were developed prior to the <code>custom_plugins.txt</code> file even being available and I never bothered to change it.</p></div><div id="comment-42420-info" class="comment-info"><span class="comment-age">(15 May '15, 08:09)</span> cmaynard ♦♦</div></div><span id="42421"></span><div id="comment-42421" class="comment"><div id="post-42421-score" class="comment-score"></div><div class="comment-text"><p>Good to know. I'll test that and see what happens.</p></div><div id="comment-42421-info" class="comment-info"><span class="comment-age">(15 May '15, 08:13)</span> coloncm</div></div><span id="42422"></span><div id="comment-42422" class="comment"><div id="post-42422-score" class="comment-score"></div><div class="comment-text"><p>Well, it appears that your instincts were dead on. My re-compilation and repackaging the portable now included the custom plugins. So, there seems to be an issue with using the inclusion of the customs_plugins.txt file on the Wireshark.nsi file when packaging for PortableApps. I might even be a path issue. I'll investigate further and I'll report it if it's not the case. Thank you.</p></div><div id="comment-42422-info" class="comment-info"><span class="comment-age">(15 May '15, 08:36)</span> coloncm</div></div></div><div id="comment-tools-42417" class="comment-tools"></div><div class="clear"></div><div id="comment-42417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

