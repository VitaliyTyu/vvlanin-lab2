<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match="/movies">
        <html>
        <head>
            <title>Movies</title>
            <style>
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
            </style>
        </head>
        <body>
            <h1>Movies</h1>
            <table>
                <tr>
                    <th>Title</th>
                    <th>Release Date</th>
                    <th>Genres</th>
                    <th>Directors</th>
                </tr>
                <xsl:for-each select="movie">
                    <tr>
                        <td><xsl:value-of select="title"/></td>
                        <td><xsl:value-of select="releaseDate"/></td>
                        <td>
                            <xsl:for-each select="genres/genre"><xsl:value-of select="."/><xsl:if test="position() != last()">, </xsl:if></xsl:for-each>
                        </td>
                        <td>
                            <xsl:for-each select="directors/director"><xsl:value-of select="."/><xsl:if test="position() != last()">, </xsl:if></xsl:for-each>
                        </td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
