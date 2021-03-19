+++
type = "question"
title = "SSL Decryption with tshark in PowerShell"
description = '''Hi all I&#x27;m trying to automate the decryption of a trace with PowerShell and tshark. I have something like this: $SSLOptions=&quot; -o ssl.desegment_ssl_records:TRUE -o ssl.desegment_ssl_application_data:TRUE -o ssl.keylog_file:C:&#92;FilesToAnalyze&#92;ssltest.sslkeys&quot; Thing is that, if I run the whole command: ...'''
date = "2017-09-26T08:38:00Z"
lastmod = "2017-09-27T00:09:00Z"
weight = 63649
keywords = [ "ssl", "tshark", "powershell" ]
aliases = [ "/questions/63649" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decryption with tshark in PowerShell](/questions/63649/ssl-decryption-with-tshark-in-powershell)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63649-score" class="post-score" title="current number of votes">0</div><span id="post-63649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I'm trying to automate the decryption of a trace with PowerShell and tshark. I have something like this:</p><p><em>$SSLOptions=" -o ssl.desegment_ssl_records:TRUE -o ssl.desegment_ssl_application_data:TRUE -o ssl.keylog_file:C:\FilesToAnalyze\ssltest.sslkeys"</em></p><p>Thing is that, if I run the whole command: <em>./tshark -r c:\FilesToAnalyze\ssltest.cap -o ssl.desegment_ssl_records:TRUE -o ssl.desegment_ssl_application_data:TRUE -o ssl.keylog_file:C:\FilesToAnalyze\ssltest.sslkeys</em></p><p>works fine. But, if I run instead</p><p><em>./tshark -r c:\FilesToAnalyze\ssltest.cap $SSLOptions</em></p><p>Fails with the following error:</p><p><strong>./tshark : tshark: "ssl.desegment_ssl_records:TRUE" was unexpected in this context. At line:1 char:1 + ./tshark -r "c:\FilesToAnalyze\ssltest.cap" $SSLOptions + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ + CategoryInfo : NotSpecified: (tshark: "ssl.de...n this context.:String) [], RemoteException + FullyQualifiedErrorId : NativeCommandError</strong></p><p>Any idea? I tested using double quotes, simple quotes, changing the order of the arguments... I have other scripts where I'm passing variables as filters or options, but I don;t know why is not working specificalyl when I use the -o option.</p><p>Thanks in advance!!</p><p>Osito</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-powershell" rel="tag" title="see questions tagged &#39;powershell&#39;">powershell</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '17, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/0e9b510379013638f59658b49d7d38cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osito&#39;s gravatar image" /><p><span>osito</span><br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osito has one accepted answer">50%</span></p></div></div><div id="comments-container-63649" class="comments-container"></div><div id="comment-tools-63649" class="comment-tools"></div><div class="clear"></div><div id="comment-63649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63655"></span>

<div id="answer-container-63655" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63655-score" class="post-score" title="current number of votes">1</div><span id="post-63655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is more a Powershell question than a Wireshark one, but here it goes. Powershell apparently interprets that as passing a single argument containing the contents of that string rather than multiple arguments for each.</p><p>A solution is to store each separate argument in an array element and use <code>@SSLOptions</code> instead of <code>$SSLOptions</code>. It works for me with Powershell 2.0 on Windows 7 x64:</p><pre><code>$file=&quot;some.pcap&quot;
[email protected](
&quot;-ossl.desegment_ssl_records:TRUE&quot;,
&quot;-ossl.desegment_ssl_application_data:TRUE&quot;,
&quot;-ossl.keylog_file:C:\FilesToAnalyze\ssltest.sslkeys&quot;
)

&amp; tshark -r $file @SSLOptions</code></pre><p>Take also advantage of the fact that tshark treats <code>-o option: value</code> the same as <code>-ooption:value</code>, that requires less array elements.</p><p>See also:</p><ul><li>Splatting (PS 2.0): <a href="https://technet.microsoft.com/en-us/library/gg675931.aspx">https://technet.microsoft.com/en-us/library/gg675931.aspx</a></li><li>Splatting (newer docs): <a href="https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting">https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting</a></li><li>Arrays: <a href="https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_arrays">https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_arrays</a></li><li>Possible helpful too: <a href="https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_escape_characters">https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_escape_characters</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '17, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-63655" class="comments-container"><span id="63656"></span><div id="comment-63656" class="comment"><div id="post-63656-score" class="comment-score"></div><div class="comment-text"><p>Hi Lekensteyn</p><p>Thanks very much for your answer, works like a charm now!! :) :)</p><p>Good to know that -o option is the same as -ooption, saves me a lot of work. And for the links, my PowwerShell is still very basic and they are interesting.</p><p>Cheers, Osito</p></div><div id="comment-63656-info" class="comment-info"><span class="comment-age">(27 Sep '17, 00:09)</span> <span class="comment-user userinfo">osito</span></div></div></div><div id="comment-tools-63655" class="comment-tools"></div><div class="clear"></div><div id="comment-63655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

