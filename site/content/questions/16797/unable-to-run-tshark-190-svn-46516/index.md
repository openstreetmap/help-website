+++
type = "question"
title = "unable to run tshark 1.9.0-SVN-46516"
description = '''Hi, I have Linux 2.6.26.8-57.fc8 i686 i686 i386 GNU/Linux. I downloaded src of wireshark 1.9.0-SVN-46516 from net and configured using ./configure --disable-gtktest --disable-wireshark --disable-warnings-as-errors. Then i did make which went through fine. Upon executing ./tshark from the directory, ...'''
date = "2012-12-12T05:39:00Z"
lastmod = "2012-12-12T07:50:00Z"
weight = 16797
keywords = [ "tshark", "linux" ]
aliases = [ "/questions/16797" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unable to run tshark 1.9.0-SVN-46516](/questions/16797/unable-to-run-tshark-190-svn-46516)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16797-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have Linux 2.6.26.8-57.fc8 i686 i686 i386 GNU/Linux.</p><p>I downloaded src of wireshark 1.9.0-SVN-46516 from net and configured using ./configure --disable-gtktest --disable-wireshark --disable-warnings-as-errors.</p><p>Then i did make which went through fine.</p><p>Upon executing ./tshark from the directory, i get following error.</p><pre><code>/export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/.libs/lt-tshark: Symbol `prefs&#39; has different size in shared object, consider re-linking

tshark: Couldn&#39;t load module /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/wimaxasncp/.libs/wimaxasncp.so: /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/wimaxasncp/.libs/wimaxasncp.so: undefined symbol: eap_type_vals_ext

tshark: Couldn&#39;t load module /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/mate/.libs/mate.so: /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/mate/.libs/mate.so: undefined symbol: prefs_register_filename_preference

tshark: Couldn&#39;t load module /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/asn1/.libs/asn1.so: /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/asn1/.libs/asn1.so: undefined symbol: prefs_register_filename_preference

tshark: Couldn&#39;t load module /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/stats_tree/.libs/stats_tree.so: /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/stats_tree/.libs/stats_tree.so: undefined symbol: stats_tree_register_plugin

tshark: Couldn&#39;t load module /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/profinet/.libs/profinet.so: /export/home/atsuser/Tools/wireshark/wireshark-1.9.0-SVN-46516/plugins/profinet/.libs/profinet.so: undefined symbol: crc16_plain_tvb_offset_seed</code></pre><p>Can someone please help me with it ?</p></div><div id="question-tags" class="tags-container tags">tshark linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '12, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/52757a3bf68018ee5b4c92c36741c626?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adianimesh&#39;s gravatar image" /><p>adianimesh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adianimesh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '12, 07:34</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-16797" class="comments-container"><span id="16811"></span><div id="comment-16811" class="comment"><div id="post-16811-score" class="comment-score"></div><div class="comment-text"><p>what is your distribution? Fedora Core 8?</p></div><div id="comment-16811-info" class="comment-info"><span class="comment-age">(12 Dec '12, 08:28)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16797" class="comment-tools"></div><div class="clear"></div><div id="comment-16797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16805"></span>

<div id="answer-container-16805" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16805-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know specifically what's wrong.</p><p>Random thought:</p><p><code>eap_type_vals_ext</code> was a very recent add to the source (defined in <code>packet-eap.c</code>).</p><p>Somehow, you've not rebuilt everything and are thus having problems.</p><p>Did you have a previous version in place before you downloaded the new source ?</p><p>In any case, since you are building from SVN, can you do a <code>make maintainer-clean</code> followed by <code>./autogen.sh</code> &amp; etc</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '12, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '12, 07:52</p></div></div><div id="comments-container-16805" class="comments-container"></div><div id="comment-tools-16805" class="comment-tools"></div><div class="clear"></div><div id="comment-16805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

