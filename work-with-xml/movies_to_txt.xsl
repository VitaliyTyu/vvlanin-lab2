<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="text" encoding="UTF-8"/>
    <xsl:template match="/movies">
        <xsl:for-each select="movie">
            Title: <xsl:value-of select="title"/>, Release Date: <xsl:value-of select="releaseDate"/>
            Genres: <xsl:for-each select="genres/genre"><xsl:value-of select="."/> <xsl:text>; </xsl:text></xsl:for-each>
            Directors: <xsl:for-each select="directors/director"><xsl:value-of select="."/> <xsl:text>; </xsl:text></xsl:for-each>
            Box Office: $<xsl:value-of select="boxOffice"/>
            
            <xsl:text>&#10;</xsl:text>
        </xsl:for-each>
    </xsl:template>
</xsl:stylesheet>
