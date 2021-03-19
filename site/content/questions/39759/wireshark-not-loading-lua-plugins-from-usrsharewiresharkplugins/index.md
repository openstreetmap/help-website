+++
type = "question"
title = "Wireshark not loading LUA plugins from /usr/share/wireshark/plugins?"
description = '''Wireshark will look for plugins at /usr/share/wireshark/plugins, according to the list of plugin directories at: B.2. Configuration Files and Folders But that doesn&#x27;t seem the case here, tested in Arch Linux and Ubuntu 14.04 with a LUA dissector. Adding the LUA dissector in the binary plugins dir (e...'''
date = "2015-02-10T05:16:00Z"
lastmod = "2015-02-12T10:52:00Z"
weight = 39759
keywords = [ "lua", "dissector", "plugin" ]
aliases = [ "/questions/39759" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not loading LUA plugins from /usr/share/wireshark/plugins?](/questions/39759/wireshark-not-loading-lua-plugins-from-usrsharewiresharkplugins)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39759-score" class="post-score" title="current number of votes">0</div><span id="post-39759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark will look for plugins at /usr/share/wireshark/plugins, according to the list of plugin directories at: <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html">B.2. Configuration Files and Folders</a></p><p>But that doesn't seem the case here, tested in Arch Linux and Ubuntu 14.04 with a LUA dissector. Adding the LUA dissector in the binary plugins dir (e.g. /usr/lib/wireshark/plugins/1.12.3 in my arch linux setup) works, though...</p><p>Any idea? What's the best way to provide custom LUA dissectors for wireshark in other packages?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/2dd03c4703283e76fedf00cade7a8c0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aleksander0m&#39;s gravatar image" /><p><span>aleksander0m</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aleksander0m has no accepted answers">0%</span></p></div></div><div id="comments-container-39759" class="comments-container"></div><div id="comment-tools-39759" class="comment-tools"></div><div class="clear"></div><div id="comment-39759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39764"></span>

<div id="answer-container-39764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39764-score" class="post-score" title="current number of votes">0</div><span id="post-39764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Wireshark will look for plugins at /usr/share/wireshark/plugins</p></blockquote><p>The paths might be different on your system due to different compile time options for different Linux distributions. You will see the paths for your system in the Wireshark GUI.</p><blockquote><p>Help -&gt; About ... -&gt; Folders</p></blockquote><p>With that information, please read the answer to the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/8328/order-of-entries-in-dissector-tables-at-startup-and-lua">https://ask.wireshark.org/questions/8328/order-of-entries-in-dissector-tables-at-startup-and-lua</a></p></blockquote><p>That should help to answer your question for your system.</p><blockquote><p>Any idea? What's the best way to provide custom LUA dissectors for wireshark in other packages?</p></blockquote><p>Well, that depends how you want to distribute your Lua dissector. The most "consistent" way would be to provide an installation package (rpm, dpkg, etc.) for your traget dsitributions, including everything: Wireshark, tshark, your Lua code, etc. However that's going to create a lot of work if you want to make your Lua code available on a lot of platforms. So the <strong>best</strong> way depends totally on <strong>your</strong> requirements ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39764" class="comments-container"><span id="39771"></span><div id="comment-39771" class="comment"><div id="post-39771-score" class="comment-score"></div><div class="comment-text"><p>Yeah, I cannot see the /usr/share/wireshark/plugins path in Help-&gt;About-&gt;Folders. But I also don't see anything specific in either the Arch or Ubuntu builds that would disable that, so I'm going to just assume that the Wireshark doc is outdated.</p><p>Regarding the distribution of the dissector; why would I want to fully repackage Wireshark just for 1 LUA file? I'll just package it to get installed in the plugins dir with its own package (as it is just a custom protocol dissector anyway).</p></div><div id="comment-39771-info" class="comment-info"><span class="comment-age">(10 Feb '15, 07:22)</span> <span class="comment-user userinfo">aleksander0m</span></div></div><span id="39774"></span><div id="comment-39774" class="comment"><div id="post-39774-score" class="comment-score"></div><div class="comment-text"><p>As I said. The <strong>best</strong> way depends on your requirements, so do it the way you need it.</p></div><div id="comment-39774-info" class="comment-info"><span class="comment-age">(10 Feb '15, 07:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-39764" class="comment-tools"></div><div class="clear"></div><div id="comment-39764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39837"></span>

<div id="answer-container-39837" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39837-score" class="post-score" title="current number of votes">0</div><span id="post-39837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the best way to distribute a Lua script is to have your users put the script into their Personal Plugins folder. The directory for this is not necessarily the same for all platforms everywhere - it's whatever is listed in <code>Help -&gt; About Wireshark -&gt; Folders -&gt; Personal Plugins</code>. It's usually <code>$HOME/.wireshark/plugins</code>, but really it's safer to just have the user look at the Help info to figure it out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '15, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39837" class="comments-container"></div><div id="comment-tools-39837" class="comment-tools"></div><div class="clear"></div><div id="comment-39837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

