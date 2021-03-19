+++
type = "question"
title = "&quot;A Field extractor must be defined before Taps or Dissectors get called&quot; when I try to create an SSL Tap"
description = '''Hi, I&#x27;m prototyping a listener in LUA using the &#x27;Evaluate Lua&#x27; window in WireShark. My goal is to access the SSL Certificate that gets exchanged during the TLS/SSL handshake. Per the data I&#x27;ve googled I have tried this: ssl_cert_Info = Field.new(&quot;ssl.handshake.certificate&quot;);  function simplelistener...'''
date = "2013-05-22T17:31:00Z"
lastmod = "2014-03-07T22:32:00Z"
weight = 21387
keywords = [ "listener", "lua", "ssl" ]
aliases = [ "/questions/21387" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["A Field extractor must be defined before Taps or Dissectors get called" when I try to create an SSL Tap](/questions/21387/a-field-extractor-must-be-defined-before-taps-or-dissectors-get-called-when-i-try-to-create-an-ssl-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21387-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm prototyping a listener in LUA using the 'Evaluate Lua' window in WireShark. My goal is to access the SSL Certificate that gets exchanged during the TLS/SSL handshake. Per the data I've googled I have tried this:</p><pre><code>ssl_cert_Info = Field.new(&quot;ssl.handshake.certificate&quot;);

function simplelistenerssl()
  local window2 = TextWindow.new(&quot;SSL Window&quot;);
  local tap = Listener.new (nil, &quot;ssl.handshake.certificate&quot;);

  function tap.packet (pinfo, buffer, userdata)
    local cert = ssl_cert_Info();

    window2:append(&quot;Certificate!\r\n&quot;);
    window2:append(tostring(cert));
  end
end</code></pre><p>When the first line (ssl_cert_info) executes, I get this error:</p><p>Lua: Error During execution of dialog callback: [string "ssl_cert_Info = Field.new("ssl");"]:1: Field_get: A Field extractor must be defined before Taps or Dissectors get called</p><p>I'm very new to Lua, though I have been using wireshark for the better part of 5 years now. Any resources or help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">listener lua ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '13, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/49cd43eda3861dc9cb90db9f5ef596c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="i68040&#39;s gravatar image" /><p>i68040<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="i68040 has no accepted answers">0%</span></p></div></div><div id="comments-container-21387" class="comments-container"></div><div id="comment-tools-21387" class="comment-tools"></div><div class="clear"></div><div id="comment-21387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30594"></span>

<div id="answer-container-30594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>[This question is quite old, but in case someone hits this in the future...]</p><p>The error message is a bit cryptic, but you got that error because you can only create Field extractors while a script is loading - because after your script loads Wireshark does some internal setup to make them usable, and it can only do that one time. So the error message says that because it assumes you're trying to create a Field at some later time, which would typically be inside a tap or listener callback, and thus the error message is written to help out people who would (incorrectly) do that in such callback functions.</p><p>In your case you're trying to do it in the evaluate console, which is also way too late to go create a Field. There are several things that cannot be done in the evaluate console - for example creating a Proto object. It's not meant as a replacement for writing a real script and loading it the normal way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 22:32</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30594" class="comments-container"></div><div id="comment-tools-30594" class="comment-tools"></div><div class="clear"></div><div id="comment-30594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

