+++
type = "question"
title = "source and destination columns"
description = '''with the advent of ipv6, these columns are hard to quickly identify with a particular system. I was wondering if there is an option to use the &quot;ethers&quot; table, when an entry exists, in place of the ip address in either the source or destination columns?'''
date = "2013-07-17T14:15:00Z"
lastmod = "2013-07-17T23:03:00Z"
weight = 23080
keywords = [ "resolution", "name-resolving", "hosts", "name", "ipv6" ]
aliases = [ "/questions/23080" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [source and destination columns](/questions/23080/source-and-destination-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23080-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>with the advent of ipv6, these columns are hard to quickly identify with a particular system. I was wondering if there is an option to use the "ethers" table, when an entry exists, in place of the ip address in either the source or destination columns?</p></div><div id="question-tags" class="tags-container tags">resolution name-resolving hosts name ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '13, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/5b1802a3dde015a758fb13baafb1605f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="proj964&#39;s gravatar image" /><p>proj964<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="proj964 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jul '13, 06:08</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-23080" class="comments-container"><span id="23081"></span><div id="comment-23081" class="comment"><div id="post-23081-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by ethers table? The MAC address vendor lookups??</p></div><div id="comment-23081-info" class="comment-info"><span class="comment-age">(17 Jul '13, 14:17)</span> Landi</div></div></div><div id="comment-tools-23080" class="comment-tools"></div><div class="clear"></div><div id="comment-23080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23092"></span>

<div id="answer-container-23092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23092-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to show the MAC addresses, or the names corresponding to the MAC addresses, in the columns in the packet summary, go to Edit -&gt; Preferences, select "Columns", and for the "Source" and "Destination" columns, select "Hardware src addr" and "Hardware dest addr", respectively.</p><p>To get the addresses mapped to names, however, you'll have to add the names to the "ethers" file; that will not happen automatically, except in cases where packets such as ARP packets, allowing Wireshark to infer the MAC address to IP address mapping and thus to translate the IP address to a host name, are in the capture. (No, Wireshark does not automatically map MAC addresses to host names.)</p><p>This will, of course, not give useful information for packets that didn't originate and terminate on your LAN segment, but that are being routed through your network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '13, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23092" class="comments-container"></div><div id="comment-tools-23092" class="comment-tools"></div><div class="clear"></div><div id="comment-23092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23090"></span>

<div id="answer-container-23090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23090-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>hosts</code> file is used for this purpose, not the <code>ethers</code> file.</p><p>For this to work, you must:</p><ul><li>Start Wireshark</li><li>Enable network resolution: <code>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Resolve network (IP) addresses -&gt; Select -&gt; OK</code></li><li>Navigate to where the <code>hosts</code> file is located: <code>Help -&gt; About Wireshark -&gt; Folders -&gt; Personal configuration -&gt; double-click on the folder</code></li><li>Create/Open your <code>hosts</code> file: If a <code>hosts</code> file already exists, open it using any text editor; if it doesn't exist, then create an empty file named <code>hosts</code> and open it.</li><li>Add the entry or entries: Each entry will have the format as documented in <a href="http://linux.die.net/man/5/hosts">man hosts</a>. For more information, see also: <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvNameResolutionSection.html">Section 7.7 Name Resolution</a> of the Wireshark user guide as well as <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html">Appendix A.2. Configuration Files and Folders</a>.</li><li>Restart Wireshark</li><li>Open a capture file or start a live capture with traffic going to/from those hosts you just added and observe that they are resolved to the host names you entered</li></ul><p>Some example entries:</p><pre><code># Comments must be prepended by the # sign!
192.168.0.1           homeserver
fdda:5cc1:23:4::1f    justin.example.com</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '13, 20:04</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '13, 20:05</p></div></div><div id="comments-container-23090" class="comments-container"><span id="23091"></span><div id="comment-23091" class="comment"><div id="post-23091-score" class="comment-score"></div><div class="comment-text"><p>Since many of the IP addresses are DHCP assigned, I don't think the hosts files is an adequate answer. Even if one is willing to accept the additional overhead of DNS lookups, there are still the multicast and broadcast packets to consider. The one thing that is constant and consistent is the relationship of the MAC to the device.</p></div><div id="comment-23091-info" class="comment-info"><span class="comment-age">(17 Jul '13, 20:26)</span> proj964</div></div><span id="23105"></span><div id="comment-23105" class="comment"><div id="post-23105-score" class="comment-score"></div><div class="comment-text"><p>If you only want name resolution for the entries in the host file to avoid DNS lookups, then you can enable the "Only use the profile hosts file preference" via: <code>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Only use the profile "hosts" file</code>.</p></div><div id="comment-23105-info" class="comment-info"><span class="comment-age">(18 Jul '13, 05:49)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-23090" class="comment-tools"></div><div class="clear"></div><div id="comment-23090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

