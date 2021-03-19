+++
type = "question"
title = "Error while dissecting the packet with my dissector on existing wireshark"
description = '''I&#x27;ve developed one wireshark dissector as a plugin .I&#x27;ve one pcap file for my protocol. It&#x27;s working fine and correctly dissecting the packet with the compiled version of wireshark. I&#x27;ve got the .dll file for that protocol.  Now i downloaded the wireshark version (1.12.5) . And placed my protocolnam...'''
date = "2015-06-10T04:58:00Z"
lastmod = "2015-06-10T08:15:00Z"
weight = 43038
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/43038" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error while dissecting the packet with my dissector on existing wireshark](/questions/43038/error-while-dissecting-the-packet-with-my-dissector-on-existing-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43038-score" class="post-score" title="current number of votes">0</div><span id="post-43038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've developed one wireshark dissector as a plugin .I've one pcap file for my protocol. It's working fine and correctly dissecting the packet with the compiled version of wireshark. I've got the .dll file for that protocol.</p><p>Now i downloaded the wireshark version (1.12.5) . And placed my protocolname.dll file to<br />
</p><blockquote><p>C:\Program Files\Wireshark\plugins\1.12.5<br />
Now when i run the wireshark with the captured file it shows the following error .</p></blockquote><pre><code>[Dissector bug, protocol FOO: proto.c:2983: failed assertion &quot;hfinfo-&gt;type == FT_STRING || hfinfo-&gt;type == FT_STRINGZ || hfinfo-&gt;type == FT_STRINGZPAD&quot;]
Expert Info (Error/Malformed): proto.c:2983: failed assertion &quot;hfinfo-&gt;type == FT_STRING || hfinfo-&gt;type == FT_STRINGZ || hfinfo-&gt;type == FT_STRINGZPAD&quot;</code></pre><p>It's correctly dissecting with the compiled version of wireshark (where i was developing) but not in the Downloaded version .why ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '15, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/ea74f093a0efe137c7c114da864fa5cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sammee%20Sharma&#39;s gravatar image" /><p><span>Sammee Sharma</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sammee Sharma has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-43038" class="comments-container"><span id="43039"></span><div id="comment-43039" class="comment"><div id="post-43039-score" class="comment-score"></div><div class="comment-text"><p>What version is your development copy of Wireshark that you used to compile the plugin?</p></div><div id="comment-43039-info" class="comment-info"><span class="comment-age">(10 Jun '15, 05:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43041"></span><div id="comment-43041" class="comment"><div id="post-43041-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> sir, it's 1.99.6[SVN Rev ] (i think it's automatically generated when u try to build the wireshark right?)</p></div><div id="comment-43041-info" class="comment-info"><span class="comment-age">(10 Jun '15, 05:40)</span> <span class="comment-user userinfo">Sammee Sharma</span></div></div></div><div id="comment-tools-43038" class="comment-tools"></div><div class="clear"></div><div id="comment-43038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43042"></span>

<div id="answer-container-43042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43042-score" class="post-score" title="current number of votes">2</div><span id="post-43042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Plugins are not binary compatible across versions. You must build your plugin for 1.2.x, ideally using the sources in the master-1.12 branch.</p><p>In addition for Windows, the plugin should also be compiled with the same version of MSVC as used for the target Wireshark to eliminate issues with different C runtime versions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43042" class="comments-container"><span id="43043"></span><div id="comment-43043" class="comment"><div id="post-43043-score" class="comment-score"></div><div class="comment-text"><p>so i should download the source code from master 1.12 branch and build the wireshark with this source file ? can you tell me about the version of msvc used for 1.12 version ?</p></div><div id="comment-43043-info" class="comment-info"><span class="comment-age">(10 Jun '15, 06:02)</span> <span class="comment-user userinfo">Sammee Sharma</span></div></div><span id="43046"></span><div id="comment-43046" class="comment"><div id="post-43046-score" class="comment-score">1</div><div class="comment-text"><p>If you use git as per the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcObtain.html">Developers Guide</a> then it's as simple as <code>git co master-1.12</code>. This will change your working copy to the head of the 1.12 branch.</p><p>If using nmake for an in-tree build, you should "clean" up your working copy before checking out the older branch; <code>nmake -f Makefile.nmake distclean</code> to clear up any build artefacts from the development build.</p></div><div id="comment-43046-info" class="comment-info"><span class="comment-age">(10 Jun '15, 06:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43047"></span><div id="comment-43047" class="comment"><div id="post-43047-score" class="comment-score"></div><div class="comment-text"><p>I've downloaded as zip file from github with branch as : master-1.12 and then extracted it. would there be any problem ?</p></div><div id="comment-43047-info" class="comment-info"><span class="comment-age">(10 Jun '15, 07:06)</span> <span class="comment-user userinfo">Sammee Sharma</span></div></div><span id="43048"></span><div id="comment-43048" class="comment"><div id="post-43048-score" class="comment-score">1</div><div class="comment-text"><p>None I can think of, apart from the fact that if you want to later build with a slightly newer version of master-1.12 you'll have to download the zip, unpack it, re-apply your changes on top of it, and then build.</p><p>Much easier using git, you can then keep your changes in their own branch and rebase them to bring in master-1.12 updates very simply.</p></div><div id="comment-43048-info" class="comment-info"><span class="comment-age">(10 Jun '15, 07:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43049"></span><div id="comment-43049" class="comment"><div id="post-43049-score" class="comment-score">1</div><div class="comment-text"><p>And for reference, Wireshark 1.12.X releases are officially built with MSVC 2010.</p></div><div id="comment-43049-info" class="comment-info"><span class="comment-age">(10 Jun '15, 07:50)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="43052"></span><div id="comment-43052" class="comment not_top_scorer"><div id="post-43052-score" class="comment-score"></div><div class="comment-text"><p>Yep, I forgot that bit, if you check the "About Wireshark" dialog, it will show which toolchain was used to build it.</p></div><div id="comment-43052-info" class="comment-info"><span class="comment-age">(10 Jun '15, 08:15)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-43042" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-43042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

