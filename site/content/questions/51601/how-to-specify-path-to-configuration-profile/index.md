+++
type = "question"
title = "How to specify path to Configuration Profile?"
description = '''Hello, I am using some Configuration Profiles with tshark to automate some testing. We want to store the config profiles in source control (Git). When I copy the profile folders from their original directory into our Git directory, tshark is unable to find them when specifying the full path. This is...'''
date = "2016-04-12T06:51:00Z"
lastmod = "2016-04-12T07:45:00Z"
weight = 51601
keywords = [ "profile", "tshark" ]
aliases = [ "/questions/51601" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to specify path to Configuration Profile?](/questions/51601/how-to-specify-path-to-configuration-profile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51601-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am using some Configuration Profiles with tshark to automate some testing. We want to store the config profiles in source control (Git). When I copy the profile folders from their original directory into our Git directory, tshark is unable to find them when specifying the full path.</p><p>This is what we want to accomplish:</p><pre><code>tshark -r C:\git\wireshark\captures\test_packets.pcapng -C C:\git\wireshark\config_profiles\NoEncryption_NoCRC</code></pre><p>However it generates this error:</p><pre><code>tshark: Configuration Profile &quot;C:\git\wireshark\config_profiles\NoEncryption_NoCRC&quot; does not exist</code></pre><p>The command below works, but I am assuming is is using the original profile that is in my User directory.</p><pre><code>tshark -r C:\git\wireshark\captures\test_packets.pcapng -C NoEncryption_NoCRC</code></pre><p>How do I specify the path to a Configuration Profile when using tshark?</p></div><div id="question-tags" class="tags-container tags">profile tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/405ab9176436b75b8303186882983cb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bakerbug&#39;s gravatar image" /><p>bakerbug<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bakerbug has no accepted answers">0%</span></p></div></div><div id="comments-container-51601" class="comments-container"></div><div id="comment-tools-51601" class="comment-tools"></div><div class="clear"></div><div id="comment-51601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51603"></span>

<div id="answer-container-51603" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51603-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can accomplish this by setting <code>WIRESHARK_APPDATA</code> to <code>C:\git\wireshark</code> and renaming <code>config_profiles</code> to <code>profiles</code>. For example:</p><pre><code>SET WIRESHARK_APPDATA=C:\git\wireshark
tshark -r C:\git\wireshark\captures\test_packets.pcapng -C NoEncryption_NoCRC</code></pre><p>Refer to the very first documented environment variable in the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '16, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-51603" class="comments-container"><span id="51612"></span><div id="comment-51612" class="comment"><div id="post-51612-score" class="comment-score"></div><div class="comment-text"><p>This method works! However, one thing to note is that the profiles must be stored in a directory called 'profiles' otherwise they won't be found. I was originally going to store them in a directory with a more descriptive name, but that is an easy thing to give up.</p></div><div id="comment-51612-info" class="comment-info"><span class="comment-age">(12 Apr '16, 14:00)</span> bakerbug</div></div></div><div id="comment-tools-51603" class="comment-tools"></div><div class="clear"></div><div id="comment-51603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51602"></span>

<div id="answer-container-51602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51602-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure if this can be done - I guess tshark is always looking into your user directory. Wireshark.exe has a command line parameter to specify the config directory like this:</p><pre><code>-P &lt;key&gt;:&lt;path&gt;          persconf:path - personal configuration files</code></pre><p>But for tshark, -P is already taken. So I don't think it's possible at the moment. Maybe open a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and file a feature request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '16, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-51602" class="comments-container"></div><div id="comment-tools-51602" class="comment-tools"></div><div class="clear"></div><div id="comment-51602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

