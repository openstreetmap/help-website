+++
type = "question"
title = "Renaming of &quot;eth&quot; dissector to &quot;eth_withoutfcs&quot;"
description = '''Renaming of &quot;eth&quot; dissector to &quot;eth_withoutfcs&quot; I asked about the usage of &quot;eth&quot; and how it was not working. Your response was prompt and timely. Thank you. For compatibility purposes I would like to know in what version this renaming occurred. I would like my dissector to run in earlier versions an...'''
date = "2016-10-17T07:13:00Z"
lastmod = "2016-10-18T01:50:00Z"
weight = 56469
keywords = [ "ethernet", "lua" ]
aliases = [ "/questions/56469" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Renaming of "eth" dissector to "eth\_withoutfcs"](/questions/56469/renaming-of-eth-dissector-to-eth_withoutfcs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56469-score" class="post-score" title="current number of votes">1</div><span id="post-56469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Renaming of "eth" dissector to "eth_withoutfcs"</p><p>I asked about the usage of "eth" and how it was not working. Your response was prompt and timely. Thank you.</p><p>For compatibility purposes I would like to know in what version this renaming occurred. I would like my dissector to run in earlier versions and I assume I can detect the current version of Wireshark and ask for the properly named ethernet dissector based on that.</p><p>Thanks Randy</p><p>So it has been suggested that I try one then then the other. I have done so with the following code.</p><pre><code>local default_dissector = Dissector.get( &quot;eth&quot; )

if ( default_dissector ~= nil ) then

    default_dissector:call( tvb , pinfo , tree )

else

    local default_dissector = Dissector.get( &quot;eth_withoutfcs&quot; )

    if ( default_dissector ~= nil ) then

        default_dissector:call( tvb , pinfo , tree )

    end
end</code></pre><p>Here is the hard error I get. Am I doing something wrong in the code up above. Lua is very new to me.</p><pre><code>Lua Error: [string &quot;D:\Applications\ThirdParty\Wireshark\Install....&quot;]:1973: bad argument #1 to &#39;get&#39; (Dissector_get: No such dissector)
    [Expert Info (Error/Undecoded): Lua Error: [string &quot;D:\Applications\ThirdParty\Wireshark\Install....&quot;]:1973: bad argument #1 to &#39;get&#39; (Dissector_get: No such dissector)]
        [Lua Error: [string &quot;D:\Applications\ThirdParty\Wireshark\Install....&quot;]:1973: bad argument #1 to &#39;get&#39; (Dissector_get: No such dissector)]
        [Severity level: Error]
        [Group: Undecoded]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '16, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/6e8b1db33a7ee4961eee9aed5627ff32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Randy%20Rohrbach&#39;s gravatar image" /><p><span>Randy Rohrbach</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Randy Rohrbach has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Oct '16, 01:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-56469" class="comments-container"></div><div id="comment-tools-56469" class="comment-tools"></div><div class="clear"></div><div id="comment-56469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56489"></span>

<div id="answer-container-56489" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56489-score" class="post-score" title="current number of votes">1</div><span id="post-56489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At the moment the Lua API throws errors whenever something unusual happens. This shows nicely in the tree, but it is not natural to the Lua programmer. As a workaround you can use <a href="https://www.lua.org/manual/5.2/manual.html#pdf-pcall"><code>pcall</code></a> to catch the error and prevent it from propagating:</p><pre><code>local success, eth_dissector = pcall(Dissector.get, &quot;eth_withoutfcs&quot;)
if not success or not eth_dissector then
    eth_dissector = Dissector.get(&quot;eth&quot;)
end</code></pre><p>Strictly speaking, <code>or not eth_dissector</code> is not necessary, but maybe the API will change to make it return <code>nil</code> for the above reasons and then you have forward compatibility.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '16, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56489" class="comments-container"></div><div id="comment-tools-56489" class="comment-tools"></div><div class="clear"></div><div id="comment-56489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

