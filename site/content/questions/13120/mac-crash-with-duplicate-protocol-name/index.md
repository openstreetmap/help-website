+++
type = "question"
title = "mac crash with &quot;Duplicate protocol name&quot;"
description = '''On Mac OS X 10.6.8, WireShark 1.8.1 will crash with &quot;Duplicate protocol name&quot;: $ wireshark  2012-07-30 11:54:01.134 defaults[766:903]  The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2012-07-30 11:54:01.143 defaults[767:903]  The domain/default pair of...'''
date = "2012-07-30T11:01:00Z"
lastmod = "2013-06-18T04:04:00Z"
weight = 13120
keywords = [ "osx", "mac", "crash", "installation" ]
aliases = [ "/questions/13120" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [mac crash with "Duplicate protocol name"](/questions/13120/mac-crash-with-duplicate-protocol-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13120-score" class="post-score" title="current number of votes">1</div><span id="post-13120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On Mac OS X 10.6.8, WireShark 1.8.1 will crash with "Duplicate protocol name":</p><pre><code>$ wireshark 
2012-07-30 11:54:01.134 defaults[766:903] 
The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist
2012-07-30 11:54:01.143 defaults[767:903] 
The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist

(process:756): Gtk-WARNING **: Locale not supported by C library.
    Using the fallback &#39;C&#39; locale.
Xlib:  extension &quot;RANDR&quot; missing on display &quot;/tmp/launch-LsbeDg/org.x:0&quot;.

(wireshark-bin:756): Gtk-WARNING **: Unable to locate theme engine in module_path: &quot;clearlooks&quot;,
11:54:01          Err  Duplicate protocol name &quot;Coseventcomm Dissector Using GIOP API&quot;! This might be caused by an inappropriate plugin or a development error.
Trace/BPT trap</code></pre><p>How to fix this? I've uninstalled, restarted, and reinstalled.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '12, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/be97ea8f6e9e94d78b828124c680a5b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paleozogt&#39;s gravatar image" /><p><span>paleozogt</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paleozogt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '12, 11:05</strong> </span></p></div></div><div id="comments-container-13120" class="comments-container"></div><div id="comment-tools-13120" class="comment-tools"></div><div class="clear"></div><div id="comment-13120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="13836"></span>

<div id="answer-container-13836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13836-score" class="post-score" title="current number of votes">1</div><span id="post-13836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>air:~ nate$ rm -rf /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/coseventcomm.*</p><p>air:~ nate$ rm -rf /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/cosnaming.*</p><p>air:~ nate$ rm -rf /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/parlay.*</p><p>air:~ nate$ rm -rf /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.*</p><p>air:~ nate$ rm -rf /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/tango.*</p><p>fixt it for me</p><p>a 'locate giop' provided no results, and there was no giop plugin...</p><p>hm</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '12, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/5c486bd5e68db1b67f9c907a33550ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="natenate19&#39;s gravatar image" /><p><span>natenate19</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="natenate19 has no accepted answers">0%</span></p></div></div><div id="comments-container-13836" class="comments-container"><span id="13889"></span><div id="comment-13889" class="comment"><div id="post-13889-score" class="comment-score"></div><div class="comment-text"><p>GIOP is the CORBA <a href="http://en.wikipedia.org/wiki/General_Inter-ORB_Protocol">General Inter-ORB Protocol</a>; Wireshark's dissector for it is built-in. The offending plugins (except for SERCOS III) are for protocols implemented atop GIOP/IIOP (just as, say, NFS is implemented atop ONC RPC). They were converted to built-in dissectors in Wireshark 1.8; as the Wireshark installer doesn't get rid of old plugins, if you install 1.8.x on top of a system with an earlier Wireshark version, you may end up with a Wireshark with a built-in and a plugin dissector for the same protocol, and hilarity ensues.</p></div><div id="comment-13889-info" class="comment-info"><span class="comment-age">(24 Aug '12, 19:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22130"></span><div id="comment-22130" class="comment"><div id="post-22130-score" class="comment-score"></div><div class="comment-text"><p>I had to rm -rf /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.* as well, but after that it launches.</p></div><div id="comment-22130-info" class="comment-info"><span class="comment-age">(18 Jun '13, 04:04)</span> <span class="comment-user userinfo">MagerValp</span></div></div></div><div id="comment-tools-13836" class="comment-tools"></div><div class="clear"></div><div id="comment-13836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13135"></span>

<div id="answer-container-13135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13135-score" class="post-score" title="current number of votes">0</div><span id="post-13135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's probably a plugin left over from an earlier installation (maybe you installed over an old version?). See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7401">bug 7401</a> and <a href="http://www.wireshark.org/lists/wireshark-users/201207/msg00085.html">this email thread</a> on the -users list.</p><p>(BTW, yes, you should presumably be allowed to install over the old version but the bug is still open.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '12, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-13135" class="comments-container"><span id="13136"></span><div id="comment-13136" class="comment"><div id="post-13136-score" class="comment-score"></div><div class="comment-text"><p>It's unclear what I should delete. I've already deleted <code>/Applications/Wireshark</code>, <code>/Library/Wireshark</code>, and <code>/Library/StartupItems/ChmodBPF</code> (as mentioned in 'Read me first.rtf') and reinstalled. Is there some other place that plugins are kept?</p></div><div id="comment-13136-info" class="comment-info"><span class="comment-age">(30 Jul '12, 14:23)</span> <span class="comment-user userinfo">paleozogt</span></div></div><span id="13138"></span><div id="comment-13138" class="comment"><div id="post-13138-score" class="comment-score"></div><div class="comment-text"><p>The email thread I referenced also talks about /Applications/Wireshark.app -- maybe that's it? (Sorry, I don't know a lot about Macs.)</p><p>~/.wireshark/plugins (your personal plugins directory) is another possibility, but it seems unlikely you'd have that plugin copied there.</p></div><div id="comment-13138-info" class="comment-info"><span class="comment-age">(30 Jul '12, 14:33)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="13890"></span><div id="comment-13890" class="comment"><div id="post-13890-score" class="comment-score"></div><div class="comment-text"><p><code>/Applications/Wireshark.app</code> is the Wireshark app bundle; it would include the plugins that ship with Wireshark. Removing it should be sufficient.</p><p>I'm not sure <em>what</em> <code>/Library/Wireshark</code> is for.</p><p><code>/Library/StartupItems/ChmodBPF</code> is just the startup item that makes the BPF devices accessible to the <code>access_bpf</code> group; there's not much need to remove it (it also lets you capture with tcpdump and so on - it's also distributed with the libpcap source).</p></div><div id="comment-13890-info" class="comment-info"><span class="comment-age">(24 Aug '12, 19:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-13135" class="comment-tools"></div><div class="clear"></div><div id="comment-13135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13139"></span>

<div id="answer-container-13139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13139-score" class="post-score" title="current number of votes">0</div><span id="post-13139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>please run Wireshark with <code>dtruss</code>.</p><blockquote><p><code>dtruss -f -t open wireshark</code><br />
</p></blockquote><p>Then check if the same plugin get's loaded from different locations. See man page of dtruss for more information.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '12, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '12, 14:58</strong> </span></p></div></div><div id="comments-container-13139" class="comments-container"><span id="13140"></span><div id="comment-13140" class="comment"><div id="post-13140-score" class="comment-score"></div><div class="comment-text"><p>dtruss outputs that its opening some of its own helpers, its dylibs, fork, and <code>/usr/local/lib/wireshark</code> and then nothing.</p></div><div id="comment-13140-info" class="comment-info"><span class="comment-age">(30 Jul '12, 15:00)</span> <span class="comment-user userinfo">paleozogt</span></div></div><span id="13141"></span><div id="comment-13141" class="comment"><div id="post-13141-score" class="comment-score"></div><div class="comment-text"><p>can you please run dtruss without "-t open" and post the output on <a href="http://pastebin.com">pastebin.com</a>?</p></div><div id="comment-13141-info" class="comment-info"><span class="comment-age">(30 Jul '12, 15:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13142"></span><div id="comment-13142" class="comment"><div id="post-13142-score" class="comment-score"></div><div class="comment-text"><p><a href="http://pastebin.com/kJNfV4d5">http://pastebin.com/kJNfV4d5</a></p></div><div id="comment-13142-info" class="comment-info"><span class="comment-age">(30 Jul '12, 15:04)</span> <span class="comment-user userinfo">paleozogt</span></div></div><span id="13143"></span><div id="comment-13143" class="comment"><div id="post-13143-score" class="comment-score"></div><div class="comment-text"><p>Do you get the same message if you run tshark? If so, please do the same for tshark?</p><blockquote><p><code>dtruss -a -f tshark</code></p></blockquote></div><div id="comment-13143-info" class="comment-info"><span class="comment-age">(30 Jul '12, 15:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13144"></span><div id="comment-13144" class="comment"><div id="post-13144-score" class="comment-score"></div><div class="comment-text"><p>tshark crashes just like wireshark does, but the dtruss output seems different: <a href="http://pastebin.com/BiXwVjFb">http://pastebin.com/BiXwVjFb</a></p></div><div id="comment-13144-info" class="comment-info"><span class="comment-age">(30 Jul '12, 15:15)</span> <span class="comment-user userinfo">paleozogt</span></div></div><span id="13145"></span><div id="comment-13145" class="comment not_top_scorer"><div id="post-13145-score" class="comment-score"></div><div class="comment-text"><p>still not what I expected :-) Both Wireshark and tshark are just shell scripts and dtruss does not follow the call of those script (for whatever reason).</p><p>So, we need to run dtruss with the real tshark binary. To figure out what is really called, I need the output of this:</p><blockquote><p><code>sh -x /usr/local/bin/tshark</code><br />
</p></blockquote><p>BTW: is ktrace available on your system?</p></div><div id="comment-13145-info" class="comment-info"><span class="comment-age">(30 Jul '12, 15:23)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-13139" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-13139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

